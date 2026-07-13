from langchain_groq import ChatGroq
from dotenv import load_dotenv
from config import LLM_MODEL

import os

load_dotenv()


def get_llm():
    """
    Returns the Groq Llama 3.1 model.
    """

    return ChatGroq(
        model=LLM_MODEL,
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0,
    )