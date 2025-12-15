import streamlit as st
import os
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
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E3A5F;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 2rem;
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
        background-color: #E3F2FD;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .quiz-answer {
        background-color: #E8F5E9;
        padding: 1rem;
        border-radius: 8px;
        margin-top: 0.5rem;
    }
    .stChatMessage {
        padding: 1rem;
    }
</style>
""", unsafe_allow_html=True)


def init_session_state():
    """Initialize session state variables."""
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
    """Check if OpenAI API key is configured."""
    return bool(os.environ.get("OPENAI_API_KEY"))


def initialize_rag() -> Tuple[bool, str]:
    """Initialize RAG engine and build index."""
    rag = get_rag_engine()
    
    if not rag.initialize():
        return False, "Не удалось инициализировать движок. Проверьте API ключ."
    
    if not rag.build_index():
        return False, "Не удалось построить индекс базы знаний."
    
    return True, "Система готова к работе!"


def display_sources(sources: List[dict]):
    """Display source documents used for the answer."""
    if not sources:
        return
    
    with st.expander("Использованные источники", expanded=False):
        for source in sources:
            st.markdown(f"""
            <div class="source-card">
                <div class="source-title">{source.get('title', 'Неизвестно')}</div>
                <div class="source-snippet">{source.get('snippet', '')}</div>
                {f'<a href="{source.get("url")}" target="_blank">Подробнее</a>' if source.get('url') else ''}
            </div>
            """, unsafe_allow_html=True)


def display_quiz(questions: List[dict]):
    """Display quiz questions for self-assessment."""
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


def main():
    init_session_state()
    
    with st.sidebar:
        st.image("https://cloud.ru/favicon.ico", width=50)
        st.title("AI-Репетитор")
        st.markdown("---")
        
        if not check_api_key():
            st.error("API ключ OpenAI не настроен. Добавьте OPENAI_API_KEY в секреты.")
            st.stop()
        
        if not st.session_state.rag_initialized:
            with st.spinner("Инициализация системы..."):
                success, message = initialize_rag()
                if success:
                    st.session_state.rag_initialized = True
                    st.success(message)
                else:
                    st.error(message)
                    st.stop()
        else:
            st.success("Система готова к работе")
        
        st.markdown("---")
        st.subheader("Настройки")
        
        st.session_state.show_sources = st.checkbox(
            "Показывать источники",
            value=st.session_state.show_sources
        )
        
        st.markdown("---")
        st.subheader("Самопроверка")
        
        quiz_topic = st.text_input("Тема для вопросов", placeholder="Например: Kubernetes")
        
        if st.button("Сгенерировать вопросы", use_container_width=True):
            if quiz_topic:
                with st.spinner("Генерация вопросов..."):
                    rag = get_rag_engine()
                    questions = rag.generate_quiz_questions(quiz_topic)
                    st.session_state.current_quiz = questions
                    st.session_state.quiz_mode = True
            else:
                st.warning("Введите тему для генерации вопросов")
        
        st.markdown("---")
        
        if st.button("Очистить историю", use_container_width=True):
            st.session_state.messages = []
            st.session_state.chat_history = []
            st.session_state.quiz_mode = False
            st.session_state.current_quiz = []
            rag = get_rag_engine()
            rag.clear_memory()
            st.rerun()
        
        st.markdown("---")
        st.markdown("""
        **Темы базы знаний:**
        - AI Factory
        - Базы данных
        - Контейнеры
        - Сети
        - Мониторинг
        - И другие...
        """)
    
    st.markdown('<div class="main-header">AI-Репетитор по техническим дисциплинам</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Ваш персональный помощник в изучении облачных технологий Cloud.ru</div>', unsafe_allow_html=True)
    
    if st.session_state.quiz_mode and st.session_state.current_quiz:
        display_quiz(st.session_state.current_quiz)
        if st.button("Вернуться к чату"):
            st.session_state.quiz_mode = False
            st.rerun()
        st.markdown("---")
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if message["role"] == "assistant" and "sources" in message and st.session_state.show_sources:
                display_sources(message["sources"])
    
    if prompt := st.chat_input("Задайте вопрос по техническим дисциплинам..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("Ищу информацию в базе знаний..."):
                rag = get_rag_engine()
                result = rag.query(prompt, st.session_state.chat_history)
                
                st.markdown(result["answer"])
                
                if st.session_state.show_sources and result.get("sources"):
                    display_sources(result["sources"])
                
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": result["answer"],
                    "sources": result.get("sources", [])
                })
                
                st.session_state.chat_history.append((prompt, result["answer"]))
    
    if not st.session_state.messages:
        st.markdown("---")
        st.markdown("### Примеры вопросов:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            example_questions = [
                "Как создать базу знаний в Managed RAG?",
                "Что такое Kubernetes и как его использовать?",
                "Как настроить PostgreSQL в Cloud.ru?"
            ]
            for q in example_questions:
                if st.button(q, key=f"example_{q[:20]}"):
                    st.session_state.messages.append({"role": "user", "content": q})
                    st.rerun()
        
        with col2:
            example_questions2 = [
                "Расскажи про Foundation Models",
                "Как работать с Kafka в облаке?",
                "Как настроить мониторинг?"
            ]
            for q in example_questions2:
                if st.button(q, key=f"example2_{q[:20]}"):
                    st.session_state.messages.append({"role": "user", "content": q})
                    st.rerun()


if __name__ == "__main__":
    main()
