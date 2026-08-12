"""Ferramenta RAG utilizada pelo agente EduAgent AI."""

from langchain_core.tools import tool

from eduagent.services.rag_service import RAGService


rag_service = RAGService()

_DOCUMENTS_INDEXED = False


def initialize_rag(path: str) -> None:
    """
    Indexa o documento que será utilizado pela ferramenta RAG.
    """

    global _DOCUMENTS_INDEXED

    rag_service.index(path)

    _DOCUMENTS_INDEXED = True


@tool
def search_documents(query: str) -> str:
    """
    Busca informações relevantes nos documentos indexados.

    Esta ferramenta realiza somente a recuperação dos documentos.
    A geração da resposta final fica sob responsabilidade do agente.
    """

    if not _DOCUMENTS_INDEXED:
        return (
            "Nenhum documento foi indexado ainda. "
            "Inicialize o RAG antes de realizar a busca."
        )

    documents = rag_service.retrieve(
        query,
        k=4,
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

    return (
        "Informações encontradas nos documentos:\n\n"
        f"{context}"
    )