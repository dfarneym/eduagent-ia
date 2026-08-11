from langchain_core.tools import tool

from eduagent.services.rag_service import RAGService


rag_service = RAGService()

_DOCUMENTS_INDEXED = False


def initialize_rag(path: str) -> None:
    """Indexa os documentos utilizados pela ferramenta RAG."""

    global _DOCUMENTS_INDEXED

    rag_service.index(path)
    _DOCUMENTS_INDEXED = True


@tool
def search_documents(query: str) -> str:
    """
    Busca informações relevantes nos documentos indexados
    utilizando o pipeline RAG.
    """

    if not _DOCUMENTS_INDEXED:
        return (
            "Nenhum documento foi indexado ainda. "
            "Inicialize o RAG antes de realizar a busca."
        )

    return rag_service.ask(query, k=4)