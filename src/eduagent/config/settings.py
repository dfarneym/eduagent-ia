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
    MODEL_NAME: str = "llama-3.3-70b-versatile"

    # Diretórios
    DOCUMENTS_PATH: str = "data/documents"
    VECTORSTORE_PATH: str = "data/vectorstore"

    # Aplicação
    APP_NAME: str = "EduAgent AI"
    APP_VERSION: str = "0.1.0"

    # Carregamento das variáveis de ambiente
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()