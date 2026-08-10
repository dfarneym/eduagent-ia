from langchain_text_splitters import RecursiveCharacterTextSplitter


class TextSplitter:
    """Responsável por dividir documentos em chunks."""

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def split(self, documents):
        """Divide os documentos em chunks."""
        return self.splitter.split_documents(documents)