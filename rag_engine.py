import os
import json
from typing import List, Dict, Any, Optional, Tuple
from pathlib import Path

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

from document_loader import prepare_documents_for_indexing

VECTOR_STORE_PATH = "vector_store"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


class RAGEngine:
    def __init__(self):
        self.embeddings = None
        self.vector_store = None
        self.llm = None
        self._initialized = False
        
    def initialize(self) -> bool:
        """Initialize the RAG engine with embeddings and LLM."""
        if not OPENAI_API_KEY:
            return False
            
        try:
            self.embeddings = OpenAIEmbeddings(
                openai_api_key=OPENAI_API_KEY,
                model="text-embedding-3-small"
            )
            
            # the newest OpenAI model is "gpt-5" which was released August 7, 2025.
            # do not change this unless explicitly requested by the user
            self.llm = ChatOpenAI(
                openai_api_key=OPENAI_API_KEY,
                model="gpt-5",
                max_completion_tokens=2048
            )
            
            self._initialized = True
            return True
        except Exception as e:
            print(f"Error initializing RAG engine: {e}")
            return False
    
    def build_index(self, force_rebuild: bool = False) -> bool:
        """Build or load the vector store index."""
        if not self._initialized:
            if not self.initialize():
                return False
        
        index_path = Path(VECTOR_STORE_PATH)
        
        if not force_rebuild and index_path.exists():
            try:
                self.vector_store = FAISS.load_local(
                    str(index_path),
                    self.embeddings,
                    allow_dangerous_deserialization=True
                )
                print("Loaded existing vector store")
                return True
            except Exception as e:
                print(f"Error loading vector store: {e}")
        
        print("Building new vector store...")
        chunks = prepare_documents_for_indexing()
        
        if not chunks:
            print("No documents found to index")
            return False
        
        documents = []
        for chunk in chunks:
            doc = Document(
                page_content=chunk["content"],
                metadata=chunk["metadata"]
            )
            documents.append(doc)
        
        self.vector_store = FAISS.from_documents(documents, self.embeddings)
        
        index_path.mkdir(parents=True, exist_ok=True)
        self.vector_store.save_local(str(index_path))
        print(f"Vector store built and saved with {len(documents)} chunks")
        
        return True
    
    def get_system_prompt(self) -> str:
        """Get the system prompt for the AI tutor."""
        return """Ты — AI-репетитор по техническим дисциплинам от Cloud.ru. Твоя задача — помогать студентам осваивать учебный материал, объяснять сложные темы простым языком и отвечать на вопросы.

Правила работы:
1. Отвечай на русском языке
2. Давай развёрнутые, понятные объяснения
3. Используй примеры из предоставленного контекста
4. Если информации недостаточно, честно скажи об этом
5. Предлагай дополнительные материалы для изучения
6. Будь дружелюбным и поддерживающим

Контекст из базы знаний:
{context}

Отвечай на вопрос студента, используя информацию из контекста выше."""
    
    def query(self, question: str, chat_history: Optional[List[Tuple[str, str]]] = None) -> Dict[str, Any]:
        """Query the RAG system with a question."""
        if not self.vector_store or not self.llm:
            return {
                "answer": "Система не инициализирована. Пожалуйста, проверьте настройки API ключа.",
                "sources": [],
                "error": True
            }
        
        try:
            relevant_docs = self.vector_store.similarity_search(question, k=5)
            
            context = "\n\n---\n\n".join([
                f"Источник: {doc.metadata.get('title', 'Неизвестно')}\n{doc.page_content}"
                for doc in relevant_docs
            ])
            
            system_prompt = self.get_system_prompt()
            
            messages = [
                SystemMessage(content=system_prompt.format(context=context))
            ]
            
            if chat_history:
                for human_msg, ai_msg in chat_history[-5:]:
                    messages.append(HumanMessage(content=human_msg))
                    messages.append(AIMessage(content=ai_msg))
            
            messages.append(HumanMessage(content=question))
            
            response = self.llm.invoke(messages)
            
            sources = []
            seen_sources = set()
            for doc in relevant_docs:
                source_key = doc.metadata.get('title', doc.metadata.get('source', 'Unknown'))
                if source_key not in seen_sources:
                    seen_sources.add(source_key)
                    sources.append({
                        "title": doc.metadata.get('title', 'Неизвестно'),
                        "source": doc.metadata.get('source', ''),
                        "url": doc.metadata.get('url', ''),
                        "section": doc.metadata.get('section', ''),
                        "snippet": doc.page_content[:200] + "..." if len(doc.page_content) > 200 else doc.page_content
                    })
            
            return {
                "answer": response.content,
                "sources": sources[:3],
                "error": False
            }
            
        except Exception as e:
            return {
                "answer": f"Произошла ошибка при обработке запроса: {str(e)}",
                "sources": [],
                "error": True
            }
    
    def generate_quiz_questions(self, topic: str, num_questions: int = 3) -> List[Dict[str, Any]]:
        """Generate quiz questions for self-assessment on a topic."""
        if not self.vector_store or not self.llm:
            return []
        
        try:
            relevant_docs = self.vector_store.similarity_search(topic, k=3)
            
            context = "\n\n".join([doc.page_content for doc in relevant_docs])
            
            prompt = f"""На основе следующего учебного материала создай {num_questions} вопроса для самопроверки студента.

Материал:
{context}

Для каждого вопроса предоставь:
1. Сам вопрос
2. Правильный ответ
3. Краткое объяснение

Формат ответа (JSON):
[
  {{"question": "...", "answer": "...", "explanation": "..."}},
  ...
]

Создавай вопросы разного уровня сложности. Отвечай только JSON без дополнительного текста."""

            response = self.llm.invoke([HumanMessage(content=prompt)])
            
            content = response.content.strip()
            if content.startswith("```"):
                content = content.split("```")[1]
                if content.startswith("json"):
                    content = content[4:]
            
            questions = json.loads(content)
            return questions
            
        except Exception as e:
            print(f"Error generating quiz questions: {e}")
            return []
    
    def query_stream(self, question: str, chat_history: Optional[List[Tuple[str, str]]] = None) -> Dict[str, Any]:
        """Query the RAG system with streaming response."""
        if not self.vector_store or not self.llm:
            return {
                "answer_stream": iter(["Система не инициализирована."]),
                "sources": [],
                "error": True
            }
        
        try:
            relevant_docs = self.vector_store.similarity_search(question, k=5)
            
            context = "\n\n---\n\n".join([
                f"Источник: {doc.metadata.get('title', 'Неизвестно')}\n{doc.page_content}"
                for doc in relevant_docs
            ])
            
            system_prompt = self.get_system_prompt()
            
            messages = [
                SystemMessage(content=system_prompt.format(context=context))
            ]
            
            if chat_history:
                for human_msg, ai_msg in chat_history[-5:]:
                    messages.append(HumanMessage(content=human_msg))
                    messages.append(AIMessage(content=ai_msg))
            
            messages.append(HumanMessage(content=question))
            
            response = self.llm.invoke(messages)
            answer = response.content
            
            def char_generator(text):
                words = text.split(' ')
                for i, word in enumerate(words):
                    yield word + (' ' if i < len(words) - 1 else '')
            
            sources = []
            seen_sources = set()
            for doc in relevant_docs:
                source_key = doc.metadata.get('title', doc.metadata.get('source', 'Unknown'))
                if source_key not in seen_sources:
                    seen_sources.add(source_key)
                    sources.append({
                        "title": doc.metadata.get('title', 'Неизвестно'),
                        "source": doc.metadata.get('source', ''),
                        "url": doc.metadata.get('url', ''),
                        "section": doc.metadata.get('section', ''),
                        "snippet": doc.page_content[:200] + "..." if len(doc.page_content) > 200 else doc.page_content
                    })
            
            return {
                "answer_stream": char_generator(answer),
                "sources": sources[:3],
                "error": False
            }
            
        except Exception as e:
            return {
                "answer_stream": iter([f"Ошибка: {str(e)}"]),
                "sources": [],
                "error": True
            }
    
    def clear_memory(self):
        """Clear conversation memory - placeholder for session-based memory."""
        pass


_rag_engine = None


def get_rag_engine() -> RAGEngine:
    """Get or create the singleton RAG engine instance."""
    global _rag_engine
    if _rag_engine is None:
        _rag_engine = RAGEngine()
    return _rag_engine
