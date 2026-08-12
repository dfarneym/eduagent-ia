"""Serviço responsável pelo pipeline RAG."""

from eduagent.services.ingest_service import IngestService
from eduagent.services.llm_service import LLMService


class RAGService:
    """Coordena ingestão, recuperação de contexto e geração de respostas."""

    def __init__(
        self,
        ingest_service: IngestService | None = None,
        llm_service: LLMService | None = None,
        score_threshold: float = 25.0,
    ):
        self.ingest_service = ingest_service or IngestService()
        self.llm_service = llm_service or LLMService()
        self.score_threshold = score_threshold

    def index(self, path: str):
        """Carrega, divide e indexa um documento."""
        return self.ingest_service.ingest(path)

    def retrieve(
        self,
        question: str,
        k: int = 4,
    ):
        """Recupera documentos relevantes utilizando similaridade."""

        if self.ingest_service.vectorstore.vectorstore is None:
            raise ValueError("Nenhum documento foi indexado.")

        results = self.ingest_service.vectorstore.search_with_score(
            question,
            k=k,
        )

        return [
            document
            for document, score in results
            if score <= self.score_threshold
        ]

    def ask(
        self,
        question: str,
        k: int = 4,
    ):
        """
        Executa o pipeline RAG e retorna a resposta com as fontes.
        """

        documents = self.retrieve(
            question,
            k=k,
        )

        if not documents:
            return (
                "Não encontrei informações relevantes "
                "nos documentos disponíveis."
            )

        context_parts = []

        for document in documents:
            context_parts.append(
                document.page_content
            )

        context = "\n\n".join(context_parts)

        prompt = f"""
Você é o EduAgent AI, um assistente educacional.

Responda à pergunta utilizando exclusivamente
as informações presentes no contexto fornecido.

Se a resposta não estiver presente no contexto,
informe claramente que a informação não foi encontrada
nos documentos.

Não invente informações.

Contexto:
{context}

Pergunta:
{question}

Responda em português de forma clara e objetiva.
"""

        response = self.llm_service.invoke(prompt)

        sources = self._format_sources(documents)

        if sources:
            return (
                f"{response.content}\n\n"
                f"---\n\n"
                f"**📚 Fontes consultadas**\n\n"
                f"{sources}"
            )

        return response.content

    @staticmethod
    def _format_sources(documents) -> str:
        """Formata os metadados dos documentos recuperados."""

        sources = []
        seen = set()

        for document in documents:
            metadata = document.metadata or {}

            source = metadata.get("source", "Documento")
            page = metadata.get("page")

            source_name = str(source).replace("\\", "/").split("/")[-1]

            if page is not None:
                label = f"`{source_name}` — página {page + 1}"
            else:
                label = f"`{source_name}`"

            if label not in seen:
                seen.add(label)
                sources.append(f"- {label}")

        return "\n".join(sources)