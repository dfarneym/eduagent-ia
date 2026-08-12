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

    results = []

    for document in documents:
        metadata = document.metadata or {}

        source = metadata.get(
            "source",
            "Documento",
        )

        page = metadata.get("page")

        source_name = (
            str(source)
            .replace("\\", "/")
            .split("/")[-1]
        )

        if page is not None:
            source_label = (
                f"{source_name} — página {page + 1}"
            )
        else:
            source_label = source_name

        results.append(
            "Fonte: "
            f"{source_label}\n"
            "Conteúdo:\n"
            f"{document.page_content}"
        )

    return (
        "Informações encontradas nos documentos:\n\n"
        + "\n\n---\n\n".join(results)
    )