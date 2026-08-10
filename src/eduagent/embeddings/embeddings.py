from langchain_huggingface import HuggingFaceEmbeddings


class Embeddings:
    """Responsável por gerar embeddings dos documentos."""

    def __init__(
        self,
        model_name: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    ):
        self.model = HuggingFaceEmbeddings(
            model_name=model_name
        )

    def embed_documents(self, documents):
        """Gera embeddings para uma lista de documentos."""
        texts = [document.page_content for document in documents]

        return self.model.embed_documents(texts)

    def embed_query(self, query: str):
        """Gera embedding para uma consulta."""
        return self.model.embed_query(query)