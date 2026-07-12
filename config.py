# config.py

from pathlib import Path

PROJECT_ROOT = Path(__file__).parent

DATA_DIR = PROJECT_ROOT / "data"

PDF_DIR = DATA_DIR / "pdfs"

VECTORSTORE_DIR = PROJECT_ROOT / "vectorstore"