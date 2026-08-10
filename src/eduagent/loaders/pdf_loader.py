'''
     -Receber um arquivo PDF
     -Responsável apenas por ler PDFs.
     -Retornar uma lista de objetos Document. 
     
'''
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


class PDFLoader:
    """
    Responsável exclusivamente pelo carregamento de arquivos PDF.
    """

    def load(self, file_path: str | Path) -> list[Document]:
        """
        Carrega um arquivo PDF e retorna uma lista de objetos Document.

        Args:
            file_path: Caminho do arquivo PDF.

        Returns:
            Lista de objetos Document.
        """

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"Arquivo PDF não encontrado: {path}"
            )

        if path.suffix.lower() != ".pdf":
            raise ValueError(
                f"O arquivo informado não é um PDF: {path}"
            )

        loader = PyPDFLoader(str(path))

        return loader.load()