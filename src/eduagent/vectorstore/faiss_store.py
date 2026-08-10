from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


class FAISSStore:
    """Responsável por criar e consultar o banco vetorial FAISS."""

    def __init__(
        self,
        embeddings: HuggingFaceEmbeddings,
    ):
        self.embeddings = embeddings
        self.vectorstore = None

    def create(self, documents):
        """Cria o banco vetorial a partir dos documentos."""
        self.vectorstore = FAISS.from_documents(
            documents,
            self.embeddings,
        )

        return self.vectorstore

    def search(self, query: str, k: int = 4):
        """Realiza uma busca por similaridade."""
        if self.vectorstore is None:
            raise ValueError("O vector store ainda não foi criado.")

        return self.vectorstore.similarity_search(
            query,
            k=k,
        )

    def as_retriever(self, k: int = 4):
        """Retorna o vector store como retriever."""
        if self.vectorstore is None:
            raise ValueError("O vector store ainda não foi criado.")

        return self.vectorstore.as_retriever(
            search_kwargs={"k": k}
        )