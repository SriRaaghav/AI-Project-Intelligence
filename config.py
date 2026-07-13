from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).parent

# Data Directories
DATA_DIR = PROJECT_ROOT / "data"
PDF_DIR = DATA_DIR / "pdfs" / "P173373"

# Vector Database
VECTORSTORE_DIR = PROJECT_ROOT / "vectorstore"

# Models
EMBEDDING_MODEL = "BAAI/bge-base-en-v1.5"
LLM_MODEL = "llama-3.1-70b-versatile"

# Chunking Configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200