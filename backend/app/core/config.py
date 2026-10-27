
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


# Find the backend folder
BASE_DIR = Path(__file__).resolve().parents[2]


# Read application settings from .env
class Settings(BaseSettings):

    # Application
    APP_NAME: str = "Tracera"
    APP_ENV: str = "development"
    DEBUG: bool = True

    # Gemini - Primary LLM
    GEMINI_API_KEY: str = ""
    GEMINI_MODEL: str = "gemini-2.5-flash"
    EMBEDDING_MODEL: str = "models/gemini-embedding-001"

    # Groq - Fallback LLM
    GROQ_API_KEY: str = ""
    GROQ_MODEL: str = "llama-3.3-70b-versatile"

    # PostgreSQL
    DATABASE_URL: str = ""

    # Pinecone
    PINECONE_API_KEY: str = ""
    PINECONE_INDEX_NAME: str = "tracera"
    PINECONE_NAMESPACE: str = "investigations"

    # LangSmith
    LANGSMITH_API_KEY: str = ""
    LANGSMITH_TRACING: bool = False
    LANGSMITH_PROJECT: str = "Tracera"

    # Locate and read the .env file
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


# Create one settings object for the application
settings = Settings()
