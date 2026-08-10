from langchain_groq import ChatGroq

from eduagent.config.settings import settings


class LLMService:
    """Responsável pela comunicação com o modelo de linguagem."""

    def __init__(self):
        if not settings.GROQ_API_KEY:
            raise ValueError(
                "GROQ_API_KEY não configurada."
            )

        self.llm = ChatGroq(
            model=settings.MODEL_NAME,
            groq_api_key=settings.GROQ_API_KEY,
            reasoning_format="hidden",
        )

    def invoke(self, prompt: str):
        """Envia uma pergunta para o modelo."""
        return self.llm.invoke(prompt)