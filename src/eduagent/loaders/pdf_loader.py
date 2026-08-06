'''
     -Receber um arquivo PDF
     -Responsável apenas por ler PDFs.
     -Retornar uma lista de objetos Document. 
     
'''
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


class PDFLoader:
    """Responsável apenas por ler PDFs."""
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self) -> list[Document]:
        if not  self.file_path.exists():
            raise FileNotFoundError("O arquivo PDF não foi encontrado.")
        
        """Carrega o PDF e retorna uma lista de objetos Document."""
        loader = PyPDFLoader(str(self.file_path))
        documents = loader.load()
        return documents
        
