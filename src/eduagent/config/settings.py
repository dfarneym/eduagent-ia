"""
Configurações da aplicação.

As variáveis podem ser carregadas automaticamente
a partir do arquivo .env.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Representa as configurações da aplicação."""

    # LLM
    GROQ_API_KEY: str = ""
    MODEL_NAME: str = "qwen/qwen3.6-27b"

    # Diretórios
    DOCUMENTS_PATH: str = "data/documents"
    VECTORSTORE_PATH: str = "data/vectorstore"

    # Aplicação
    APP_NAME: str = "EduAgent AI"
    APP_VERSION: str = "0.1.0"

    # Limites da aplicação
    MAX_FILE_SIZE_MB: int = 10
    MAX_PAGES: int = 50
    MAX_QUESTION_CHARS: int = 2000
    MAX_HISTORY_MESSAGES: int = 10

    # Carregamento das variáveis de ambiente
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()