"""
Essa BaseSettings importação permite carregar automaticamente as configurações
do arquivo .env.
Já SettingsConfigDict informa ao Pydantic onde está o  .env
e como ele deve ser lido
"""
from pydantic_settings import BaseSettings, SettingsConfigDict

# Essa classe representa todas as configurações da aplicação
class Settings(BaseSettings):
    # LLM
    GOOGLE_API_KEY: str = ""
    MODEL_NAME: str = "gemini-3.1-flash-lite"

    # DiretóriosEvitamos de escrever vários arquivos
    DOCUMENTS_PATH: str = "data/documents"
    VECTORSTORE_PATH: str = "data/vectorstore"

    # Aplicação
    APP_NAME: str = "EduAgent AI"
    APP_VERSION: str = "0.1.0"

    #Lendo as variaveis de ambiente do arquivo .env
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    
    )

# Essa vai ser a instancia utilizada em toda a aplicação
settings = Settings()
