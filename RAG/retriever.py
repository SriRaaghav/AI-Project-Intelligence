from langchain_community.vectorstores import FAISS

from config import VECTORSTORE_DIR
from rag.embeddings import get_embedding_model


def load_vectorstore():
    """
    Load the saved FAISS vector database.
    """

    embeddings = get_embedding_model()

    return FAISS.load_local(
        str(VECTORSTORE_DIR),
        embeddings,
        allow_dangerous_deserialization=True
    )


def get_retriever(k=5):
    """
    Return a retriever for semantic search.
    """

    vectorstore = load_vectorstore()

    return vectorstore.as_retriever(
        search_kwargs={"k": k}
    )