from typing import Any, List
from typing_extensions import TypedDict

from langchain_core.documents import Document


class ChatState(TypedDict):

    question: str

    documents: List[Document]

    response: str