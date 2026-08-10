from eduagent.vectorstore.faiss_store import FAISSStore


class Retriever:
    """Responsável por recuperar documentos relevantes."""

    def __init__(self, vectorstore: FAISSStore):
        self.vectorstore = vectorstore

    def search(self, query: str, k: int = 4):
        """Busca os documentos mais relevantes para uma consulta."""
        return self.vectorstore.search(
            query,
            k=k,
        )