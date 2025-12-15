import streamlit as st
import os
import time
from typing import List, Tuple

from rag_engine import get_rag_engine, RAGEngine

st.set_page_config(
    page_title="AI-Репетитор | Cloud.ru",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @font-face {
        font-family: 'Factor A';
        src: url('app/static/fonts/FactorA-Regular.ttf') format('truetype');
        font-weight: normal;
    }
    @font-face {
        font-family: 'Factor A';
        src: url('app/static/fonts/FactorA-Bold.ttf') format('truetype');
        font-weight: bold;
    }
    
    html, body, [class*="css"] {
        font-family: 'Factor A', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .source-card {
        background-color: #f8f9fa;
        border-left: 4px solid #1E88E5;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 0 8px 8px 0;
    }
    .source-title {
        font-weight: bold;
        color: #1E3A5F;
    }
    .source-snippet {
        font-size: 0.9rem;
        color: #666;
        margin-top: 0.5rem;
    }
    .quiz-question {
        background-color: #2d3748;
        color: #ffffff;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 4px solid #4299e1;
    }
    .quiz-answer {
        background-color: #1a202c;
        color: #e2e8f0;
        padding: 1rem;
        border-radius: 8px;
        margin-top: 0.5rem;
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .stChatMessage {
        animation: fadeInUp 0.3s ease-out;
    }
    
    .thinking-indicator {
        display: flex;
        align-items: center;
        gap: 8px;
        color: #666;
        font-style: italic;
        padding: 0.5rem 0;
    }
    
    .thinking-dot {
        width: 8px;
        height: 8px;
        background-color: #1E88E5;
        border-radius: 50%;
        animation: pulse 1.4s ease-in-out infinite;
    }
    
    .thinking-dot:nth-child(2) { animation-delay: 0.2s; }
    .thinking-dot:nth-child(3) { animation-delay: 0.4s; }
    
    @keyframes pulse {
        0%, 80%, 100% { opacity: 0.3; transform: scale(0.8); }
        40% { opacity: 1; transform: scale(1); }
    }
</style>
""", unsafe_allow_html=True)


def init_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "rag_initialized" not in st.session_state:
        st.session_state.rag_initialized = False
    if "show_sources" not in st.session_state:
        st.session_state.show_sources = True
    if "quiz_mode" not in st.session_state:
        st.session_state.quiz_mode = False
    if "current_quiz" not in st.session_state:
        st.session_state.current_quiz = []


def check_api_key() -> bool:
    return bool(os.environ.get("OPENAI_API_KEY"))


def initialize_rag() -> Tuple[bool, str]:
    rag = get_rag_engine()
    
    if not rag.initialize():
        return False, "Не удалось инициализировать движок. Проверьте API ключ."
    
    if not rag.build_index():
        return False, "Не удалось построить индекс базы знаний."
    
    return True, "Система готова к работе!"


def display_sources(sources: List[dict]):
    if not sources:
        return
    
    with st.expander("📚 Использованные источники", expanded=False):
        for source in sources:
            st.markdown(f"""
            <div class="source-card">
                <div class="source-title">{source.get('title', 'Неизвестно')}</div>
                <div class="source-snippet">{source.get('snippet', '')}</div>
                {f'<a href="{source.get("url")}" target="_blank">Подробнее</a>' if source.get('url') else ''}
            </div>
            """, unsafe_allow_html=True)


def display_quiz(questions: List[dict]):
    if not questions:
        st.warning("Не удалось сгенерировать вопросы. Попробуйте другую тему.")
        return
    
    st.subheader("Вопросы для самопроверки")
    
    for i, q in enumerate(questions, 1):
        st.markdown(f"""
        <div class="quiz-question">
            <strong>Вопрос {i}:</strong> {q.get('question', '')}
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander(f"Показать ответ на вопрос {i}"):
            st.markdown(f"""
            <div class="quiz-answer">
                <strong>Ответ:</strong> {q.get('answer', '')}
                <br><br>
                <strong>Объяснение:</strong> {q.get('explanation', '')}
            </div>
            """, unsafe_allow_html=True)


def stream_response(rag, prompt, chat_history):
    result = rag.query_stream(prompt, chat_history)
    return result


def main():
    init_session_state()
    
    with st.sidebar:
        st.title("🎓 AI-Репетитор")
        st.caption("Cloud.ru")
        st.markdown("---")
        
        if not check_api_key():
            st.error("API ключ OpenAI не настроен.")
            st.stop()
        
        if not st.session_state.rag_initialized:
            with st.spinner("Инициализация..."):
                success, message = initialize_rag()
                if success:
                    st.session_state.rag_initialized = True
                else:
                    st.error(message)
                    st.stop()
        
        st.markdown("---")
        
        st.session_state.show_sources = st.checkbox(
            "Показывать источники",
            value=st.session_state.show_sources
        )
        
        st.markdown("---")
        st.subheader("📝 Самопроверка")
        
        quiz_topic = st.text_input("Тема", placeholder="Например: Kubernetes")
        
        if st.button("Сгенерировать вопросы", use_container_width=True):
            if quiz_topic:
                with st.spinner("Генерация..."):
                    rag = get_rag_engine()
                    questions = rag.generate_quiz_questions(quiz_topic)
                    st.session_state.current_quiz = questions
                    st.session_state.quiz_mode = True
                    st.rerun()
            else:
                st.warning("Введите тему")
        
        st.markdown("---")
        
        if st.button("🗑️ Очистить историю", use_container_width=True):
            st.session_state.messages = []
            st.session_state.chat_history = []
            st.session_state.quiz_mode = False
            st.session_state.current_quiz = []
            rag = get_rag_engine()
            rag.clear_memory()
            st.rerun()
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if message["role"] == "assistant" and "sources" in message and st.session_state.show_sources:
                display_sources(message["sources"])
    
    if prompt := st.chat_input("Задайте вопрос..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            thinking_placeholder = st.empty()
            thinking_placeholder.markdown("""
            <div class="thinking-indicator">
                <div class="thinking-dot"></div>
                <div class="thinking-dot"></div>
                <div class="thinking-dot"></div>
                <span>Анализирую базу знаний...</span>
            </div>
            """, unsafe_allow_html=True)
            
            rag = get_rag_engine()
            result = rag.query_stream(prompt, st.session_state.chat_history)
            
            thinking_placeholder.empty()
            
            response_placeholder = st.empty()
            full_response = ""
            
            for chunk in result["answer_stream"]:
                full_response += chunk
                response_placeholder.markdown(full_response + "▌")
                time.sleep(0.02)
            
            response_placeholder.markdown(full_response)
            
            if st.session_state.show_sources and result.get("sources"):
                display_sources(result["sources"])
            
            st.session_state.messages.append({
                "role": "assistant",
                "content": full_response,
                "sources": result.get("sources", [])
            })
            
            st.session_state.chat_history.append((prompt, full_response))
    
    if st.session_state.quiz_mode and st.session_state.current_quiz:
        display_quiz(st.session_state.current_quiz)
        if st.button("← Скрыть вопросы"):
            st.session_state.quiz_mode = False
            st.session_state.current_quiz = []
            st.rerun()
    
    if not st.session_state.messages and not st.session_state.quiz_mode:
        st.markdown("### Примеры вопросов:")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Как создать базу знаний в Managed RAG?", key="ex1"):
                st.session_state.messages.append({"role": "user", "content": "Как создать базу знаний в Managed RAG?"})
                st.rerun()
            if st.button("Что такое Kubernetes?", key="ex2"):
                st.session_state.messages.append({"role": "user", "content": "Что такое Kubernetes?"})
                st.rerun()
            if st.button("Как настроить PostgreSQL?", key="ex3"):
                st.session_state.messages.append({"role": "user", "content": "Как настроить PostgreSQL?"})
                st.rerun()
        
        with col2:
            if st.button("Расскажи про Foundation Models", key="ex4"):
                st.session_state.messages.append({"role": "user", "content": "Расскажи про Foundation Models"})
                st.rerun()
            if st.button("Как работать с Kafka?", key="ex5"):
                st.session_state.messages.append({"role": "user", "content": "Как работать с Kafka?"})
                st.rerun()
            if st.button("Как настроить мониторинг?", key="ex6"):
                st.session_state.messages.append({"role": "user", "content": "Как настроить мониторинг?"})
                st.rerun()


if __name__ == "__main__":
    main()
