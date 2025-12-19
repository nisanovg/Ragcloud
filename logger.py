import logging
import json
import sys
from datetime import datetime
from typing import Any, Optional


class JSONFormatter(logging.Formatter):
    """Custom JSON formatter for structured logging."""
    
    def format(self, record: logging.LogRecord) -> str:
        log_data = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        
        if hasattr(record, 'extra_data'):
            log_data.update(record.extra_data)
        
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        
        return json.dumps(log_data, ensure_ascii=False)


def setup_logger(name: str = "ai_tutor") -> logging.Logger:
    """Setup structured logger for the application."""
    logger = logging.getLogger(name)
    
    if logger.handlers:
        return logger
    
    logger.setLevel(logging.INFO)
    
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(JSONFormatter())
    logger.addHandler(console_handler)
    
    file_handler = logging.FileHandler("app.log", encoding="utf-8")
    file_handler.setFormatter(JSONFormatter())
    logger.addHandler(file_handler)
    
    return logger


def log_with_context(logger: logging.Logger, level: str, message: str, **kwargs):
    """Log message with additional context data."""
    record = logging.LogRecord(
        name=logger.name,
        level=getattr(logging, level.upper()),
        pathname="",
        lineno=0,
        msg=message,
        args=(),
        exc_info=None
    )
    record.extra_data = kwargs
    logger.handle(record)


class MetricsCollector:
    """Simple in-memory metrics collector."""
    
    def __init__(self):
        self.request_count = 0
        self.error_count = 0
        self.total_response_time = 0.0
        self.guard_violations = 0
        self.session_start = datetime.utcnow()
    
    def record_request(self, response_time: float, success: bool = True):
        """Record a request with timing."""
        self.request_count += 1
        self.total_response_time += response_time
        if not success:
            self.error_count += 1
    
    def record_guard_violation(self):
        """Record a content guard violation."""
        self.guard_violations += 1
    
    def get_stats(self) -> dict:
        """Get current metrics."""
        avg_time = (self.total_response_time / self.request_count 
                   if self.request_count > 0 else 0)
        return {
            "total_requests": self.request_count,
            "error_count": self.error_count,
            "avg_response_time_sec": round(avg_time, 2),
            "guard_violations": self.guard_violations,
            "uptime_sec": (datetime.utcnow() - self.session_start).total_seconds()
        }


logger = setup_logger()
metrics = MetricsCollector()


MAX_INPUT_LENGTH = 2000
MIN_INPUT_LENGTH = 2


def validate_user_input(text: str) -> tuple[bool, str]:
    """
    Validate user input for safety and limits.
    Returns (is_valid, error_message).
    """
    if not text or not text.strip():
        return False, "Пожалуйста, введите вопрос."
    
    text = text.strip()
    
    if len(text) < MIN_INPUT_LENGTH:
        return False, "Вопрос слишком короткий."
    
    if len(text) > MAX_INPUT_LENGTH:
        return False, f"Вопрос слишком длинный (максимум {MAX_INPUT_LENGTH} символов)."
    
    return True, ""


def sanitize_error_message(error: Exception) -> str:
    """Convert raw exception to user-friendly message."""
    error_str = str(error).lower()
    
    if "api" in error_str or "key" in error_str or "auth" in error_str:
        return "Ошибка подключения к сервису. Попробуйте позже."
    
    if "timeout" in error_str or "connection" in error_str:
        return "Сервис временно недоступен. Попробуйте позже."
    
    if "rate" in error_str or "limit" in error_str:
        return "Превышен лимит запросов. Подождите немного."
    
    return "Произошла ошибка. Попробуйте переформулировать вопрос."
