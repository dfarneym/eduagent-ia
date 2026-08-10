"""Serviço responsável pelo pipeline RAG."""

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

        self.vectorstore = None
        self.score_threshold = score_threshold

    def index(self, path: str):
        """Carrega, divide e indexa um documento."""

        chunks = self.ingest_service.ingest(path)

        self.vectorstore = self.ingest_service.vectorstore.create(
            chunks
        )

        return chunks

    def retrieve(
        self,
        question: str,
        k: int = 4,
    ):
        """Recupera documentos relevantes."""

        if self.vectorstore is None:
            raise ValueError(
                "Nenhum documento foi indexado."
            )

        results = self.ingest_service.vectorstore.search_with_score(
            question,
            k=k,
        )

        relevant_documents = [
            document
            for document, score in results
            if score <= self.score_threshold
        ]

        return relevant_documents

    def ask(
        self,
        question: str,
        k: int = 4,
    ):
        """Recupera contexto relevante e gera uma resposta."""

        documents = self.retrieve(
            question,
            k=k,
        )

        if not documents:
            return (
                "Não encontrei informações relevantes "
                "nos documentos disponíveis."
            )

        context = "\n\n".join(
            document.page_content
            for document in documents
        )

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

        return response.content