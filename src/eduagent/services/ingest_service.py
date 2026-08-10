# Responsável por coordenar o processo de ingestão de documentos.

from eduagent.loaders import PDFLoader
from eduagent.splitters.text_splitter import TextSplitter
from eduagent.embeddings.embeddings import Embeddings
from eduagent.vectorstore.faiss_store import FAISSStore


class IngestService:
    """Coordena o pipeline de ingestão de documentos."""

    def __init__(
        self,
        loader: PDFLoader | None = None,
        splitter: TextSplitter | None = None,
        embeddings: Embeddings | None = None,
        vectorstore: FAISSStore | None = None,
    ):
        self.loader = loader or PDFLoader()
        self.splitter = splitter or TextSplitter()
        self.embeddings = embeddings or Embeddings()
        self.vectorstore = vectorstore or FAISSStore(
            self.embeddings.model
        )

    def ingest(self, path: str):
        """Carrega o documento e cria o índice vetorial."""

        documents = self.loader.load(path)
        chunks = self.splitter.split(documents)

        self.vectorstore.create(chunks)

        return chunks