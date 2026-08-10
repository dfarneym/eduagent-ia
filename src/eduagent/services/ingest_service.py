# Responsável por coordenar o processo de ingestão de documentos.
from eduagent.loaders import PDFLoader
from eduagent.splitters.text_splitter import TextSplitter


class IngestService:
    """Orquestra o processo de ingestão de documentos."""

    def __init__(
        self,
        loader: PDFLoader | None = None,
        splitter: TextSplitter | None = None,
    ):
        self.loader = loader or PDFLoader()
        self.splitter = splitter or TextSplitter()

    def ingest(self, path: str):
        """Carrega um documento e transforma seu conteúdo em chunks."""
        documents = self.loader.load(path)
        chunks = self.splitter.split(documents)

        return chunks