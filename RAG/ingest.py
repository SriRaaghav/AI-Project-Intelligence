# Read PDFs and prepare them for indexing.

from pathlib import Path

from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import PDF_DIR


def load_documents():
    """
    Load all PDF documents from the data/pdfs directory.
    """

    documents = []

    for pdf_file in PDF_DIR.glob("*.pdf"):
        loader = PyMuPDFLoader(str(pdf_file))
        documents.extend(loader.load())

    return documents


def split_documents(documents):
    """
    Split documents into smaller chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    return splitter.split_documents(documents)