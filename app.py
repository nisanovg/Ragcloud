import streamlit as st
import os
import time
from typing import List, Tuple

from rag_engine import get_rag_engine, RAGEngine
from logger import logger, metrics, validate_user_input, sanitize_error_message, log_with_context

st.set_page_config(
    page_title="AI-Репетитор | Cloud.ru",
    page_icon="💡",
    layout="centered",
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
    
    .stTextInput input:focus, .stChatInput textarea:focus {
        border-color: #8B5CF6 !important;
        box-shadow: 0 0 0 1px #8B5CF6 !important;
    }
    
    .stTextInput div[data-testid="InputInstructions"] {
        display: none !important;
    }
    
    
    div[data-baseweb="input"]:focus-within {
        border-color: #8B5CF6 !important;
    }
    
    .stChatInput > div:focus-within {
        border-color: #8B5CF6 !important;
        box-shadow: 0 0 0 1px #8B5CF6 !important;
    }
</style>
""", unsafe_allow_html=True)


def load_knowledge_bases():
    """Load knowledge bases config from external JSON file."""
    config_path = "knowledge_bases.json"
    try:
        import json
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        kb_dict = {}
        for kb in config.get("knowledge_bases", []):
            kb_dict[kb["id"]] = {
                "name": kb["name"],
                "path": kb["path"],
                "enabled": kb["enabled"],
                "description": kb.get("description", "")
            }
        return kb_dict
    except Exception as e:
        print(f"Error loading knowledge bases config: {e}")
        return {
            "cloudru": {"name": "Cloud.ru", "path": "knowledge_base/cloudru", "enabled": True}
        }

KNOWLEDGE_BASES = load_knowledge_bases()

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
        st.session_state.current_quiz = {"questions": [], "sources": []}
    if "pending_question" not in st.session_state:
        st.session_state.pending_question = None
    if "processing" not in st.session_state:
        st.session_state.processing = False
    if "awaiting_response" not in st.session_state:
        st.session_state.awaiting_response = False
    if "selected_kb" not in st.session_state:
        st.session_state.selected_kb = "cloudru"


def check_api_key() -> bool:
    return bool(os.environ.get("OPENAI_API_KEY"))


def initialize_rag(knowledge_base_path: str = "knowledge_base/cloudru") -> Tuple[bool, str]:
    rag = get_rag_engine()
    
    if not rag.initialize():
        return False, "Не удалось инициализировать движок. Проверьте API ключ."
    
    if not rag.build_index(knowledge_base_path=knowledge_base_path):
        return False, "Не удалось построить индекс базы знаний."
    
    return True, "Система готова к работе!"


def display_sources(sources: List[dict]):
    if not sources:
        return
    
    with st.expander("📖 Использованные источники", expanded=False):
        for source in sources:
            st.markdown(f"""
            <div class="source-card">
                <div class="source-title">{source.get('title', 'Неизвестно')}</div>
                <div class="source-snippet">{source.get('snippet', '')}</div>
                {f'<a href="{source.get("url")}" target="_blank">Подробнее</a>' if source.get('url') else ''}
            </div>
            """, unsafe_allow_html=True)


def display_recommendations(recommendations: List[dict]):
    if not recommendations:
        return
    
    with st.expander("📚 Рекомендуемые материалы для изучения", expanded=False):
        for rec in recommendations:
            url_link = f'<a href="{rec.get("url")}" target="_blank">Открыть</a>' if rec.get('url') else ''
            st.markdown(f"""
            <div class="source-card" style="border-left-color: #10B981;">
                <div class="source-title" style="color: #10B981;">{rec.get('title', 'Материал')}</div>
                <div class="source-snippet">{rec.get('description', '')}</div>
                {url_link}
            </div>
            """, unsafe_allow_html=True)


def display_quiz(quiz_data: dict):
    questions = quiz_data.get("questions", [])
    sources = quiz_data.get("sources", [])
    
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
    
    if sources:
        display_sources(sources)


def stream_response(rag, prompt, chat_history):
    result = rag.query_stream(prompt, chat_history)
    return result


def main():
    init_session_state()
    
    with st.sidebar:
        st.title("💡 AI-Репетитор")
        st.caption("Cloud.ru")
        
        if not check_api_key():
            st.error("API ключ OpenAI не настроен.")
            st.stop()
        
        st.markdown("---")
        st.subheader("📚 База знаний")
        
        kb_options = list(KNOWLEDGE_BASES.keys())
        
        def format_kb(kb_id):
            kb_info = KNOWLEDGE_BASES[kb_id]
            if kb_info["enabled"]:
                return kb_info["name"]
            return f"🔒 {kb_info['name']} (скоро)"
        
        current_idx = kb_options.index(st.session_state.selected_kb) if st.session_state.selected_kb in kb_options else 0
        
        selected = st.selectbox(
            "Выберите предмет",
            options=kb_options,
            index=current_idx,
            format_func=format_kb,
            label_visibility="collapsed"
        )
        
        if not KNOWLEDGE_BASES[selected]["enabled"]:
            st.warning("Эта база знаний пока недоступна.")
            selected = st.session_state.selected_kb
        
        if selected != st.session_state.selected_kb:
            st.session_state.selected_kb = selected
            st.session_state.rag_initialized = False
            st.session_state.messages = []
            st.session_state.chat_history = []
            st.rerun()
        
        if not st.session_state.rag_initialized:
            with st.spinner("Инициализация..."):
                kb_path = KNOWLEDGE_BASES[st.session_state.selected_kb]["path"]
                success, message = initialize_rag(kb_path)
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
        st.subheader("✏️ Самопроверка")
        
        quiz_topic = st.text_input("Тема", placeholder="Например: Kubernetes", label_visibility="collapsed")
        
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
        
        if st.button("Очистить историю", use_container_width=True):
            st.session_state.messages = []
            st.session_state.chat_history = []
            st.session_state.quiz_mode = False
            st.session_state.current_quiz = {"questions": [], "sources": []}
            st.session_state.awaiting_response = False
            st.session_state.pending_question = None
            rag = get_rag_engine()
            rag.clear_memory()
            st.rerun()
    
    need_response = False
    current_question = None
    
    if st.session_state.pending_question:
        pending = st.session_state.pending_question
        st.session_state.pending_question = None
        is_valid, validation_error = validate_user_input(pending)
        if is_valid:
            current_question = pending
            st.session_state.messages.append({"role": "user", "content": current_question})
            st.session_state.awaiting_response = True
            need_response = True
        else:
            st.warning(validation_error)
    elif st.session_state.awaiting_response and st.session_state.messages:
        if st.session_state.messages[-1]["role"] == "user":
            current_question = st.session_state.messages[-1]["content"]
            need_response = True
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if message["role"] == "assistant":
                if "sources" in message and st.session_state.show_sources:
                    display_sources(message["sources"])
                if "recommendations" in message and message["recommendations"]:
                    display_recommendations(message["recommendations"])
    
    examples_container = st.empty()
    
    if not st.session_state.messages and not st.session_state.quiz_mode and not st.session_state.awaiting_response:
        with examples_container.container():
            st.markdown("<div style='margin-top: 40vh;'></div>", unsafe_allow_html=True)
            st.markdown("### Примеры вопросов:")
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("Как создать базу знаний в Managed RAG?", key="ex1"):
                    st.session_state.pending_question = "Как создать базу знаний в Managed RAG?"
                    st.rerun()
                if st.button("Что такое Kubernetes?", key="ex2"):
                    st.session_state.pending_question = "Что такое Kubernetes?"
                    st.rerun()
                if st.button("Как настроить PostgreSQL?", key="ex3"):
                    st.session_state.pending_question = "Как настроить PostgreSQL?"
                    st.rerun()
            
            with col2:
                if st.button("Расскажи про Foundation Models", key="ex4"):
                    st.session_state.pending_question = "Расскажи про Foundation Models"
                    st.rerun()
                if st.button("Как работать с Kafka?", key="ex5"):
                    st.session_state.pending_question = "Как работать с Kafka?"
                    st.rerun()
                if st.button("Как настроить мониторинг?", key="ex6"):
                    st.session_state.pending_question = "Как настроить мониторинг?"
                    st.rerun()
    
    is_disabled = st.session_state.awaiting_response
    chat_prompt = st.chat_input("Задайте вопрос...", disabled=is_disabled)
    
    if chat_prompt and not is_disabled:
        is_valid, validation_error = validate_user_input(chat_prompt)
        if not is_valid:
            st.warning(validation_error)
        else:
            current_question = chat_prompt
            st.session_state.messages.append({"role": "user", "content": current_question})
            st.session_state.awaiting_response = True
            need_response = True
            with st.chat_message("user"):
                st.markdown(current_question)
    
    if need_response and current_question:
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
            
            start_time = time.time()
            
            try:
                log_with_context(logger, "info", "User query received",
                    query_length=len(current_question),
                    kb=st.session_state.selected_kb,
                    history_length=len(st.session_state.chat_history))
                
                rag = get_rag_engine()
                result = rag.query_stream(current_question, st.session_state.chat_history)
                
                thinking_placeholder.empty()
                
                response_placeholder = st.empty()
                full_response = ""
                
                for chunk in result["answer_stream"]:
                    full_response += chunk
                    response_placeholder.markdown(full_response + "▌")
                    time.sleep(0.02)
                
                response_placeholder.markdown(full_response)
                
                response_time = time.time() - start_time
                metrics.record_request(response_time, success=True)
                
                log_with_context(logger, "info", "Query completed",
                    response_time=round(response_time, 2),
                    sources_count=len(result.get("sources", [])),
                    response_length=len(full_response))
                
                if st.session_state.show_sources and result.get("sources"):
                    display_sources(result["sources"])
                
                if result.get("recommendations"):
                    display_recommendations(result["recommendations"])
                
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": full_response,
                    "sources": result.get("sources", []),
                    "recommendations": result.get("recommendations", [])
                })
                
                st.session_state.chat_history.append((current_question, full_response))
                
            except Exception as e:
                response_time = time.time() - start_time
                metrics.record_request(response_time, success=False)
                
                log_with_context(logger, "error", "Query failed",
                    error_type=type(e).__name__,
                    response_time=round(response_time, 2))
                
                thinking_placeholder.empty()
                user_friendly_error = sanitize_error_message(e)
                st.error(user_friendly_error)
            finally:
                st.session_state.awaiting_response = False
                st.rerun()
    
    if st.session_state.quiz_mode and st.session_state.current_quiz.get("questions"):
        display_quiz(st.session_state.current_quiz)
        if st.button("← Скрыть вопросы"):
            st.session_state.quiz_mode = False
            st.session_state.current_quiz = {"questions": [], "sources": []}
            st.rerun()


if __name__ == "__main__":
    main()
