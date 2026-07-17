from typing import TypedDict, List, Any


class GraphState(TypedDict):

    question: str

    agent: str

    response: str

    sources: List[Any]