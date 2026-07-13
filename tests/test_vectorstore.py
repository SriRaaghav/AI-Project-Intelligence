from rag.ingest import load_documents, split_documents
from rag.cleaner import clean_documents
from rag.vectorstore import create_vectorstore

documents = load_documents()

documents = clean_documents(documents)

chunks = split_documents(documents)

vectorstore = create_vectorstore(chunks)

print("FAISS Index Created Successfully!")