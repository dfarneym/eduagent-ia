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
        """
        Carrega, divide e indexa um documento.

        Retorna os chunks gerados durante a ingestão.
        """

        chunks = self.ingest_service.ingest(path)

        return chunks

    def retrieve(
        self,
        question: str,
        k: int = 4,
    ):
        """
        Recupera documentos relevantes utilizando similaridade
        e aplica o filtro de score.
        """

        if self.ingest_service.vectorstore.vectorstore is None:
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
        """
        Executa um pipeline RAG tradicional.

        Recupera os documentos relevantes e utiliza o LLM
        para gerar uma resposta baseada exclusivamente no contexto.
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