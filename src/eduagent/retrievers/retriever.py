from langchain_core.documents import Document


class Retriever:
    """Responsável por recuperar documentos relevantes."""

    def __init__(self, vectorstore):
        self.vectorstore = vectorstore

    def search(self, query: str, k: int = 4) -> list[Document]:
        """Busca documentos relevantes para uma consulta."""
        return self.vectorstore.similarity_search(
            query,
            k=k,
        )