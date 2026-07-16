from abc import ABC, abstractmethod

from rag.llm import get_llm
from rag.retriever import retrieve_context


class BaseAgent(ABC):
    """
    Base class for all AI agents.
    """

    def __init__(self):

        self.llm = get_llm()

    @property
    @abstractmethod
    def QUERY(self):
        """
        Retrieval query.
        """
        pass

    @property
    @abstractmethod
    def PROMPT(self):
        """
        LangChain PromptTemplate.
        """
        pass

    def retrieve(self):

        return retrieve_context(
            self.QUERY,
            k=10
        )

    def build_context(self, docs):

        return "\n\n".join(
            doc.page_content
            for doc in docs
        )

    def run(self):

        docs = self.retrieve()

        context = self.build_context(docs)

        messages = self.PROMPT.format_messages(
            context=context
        )

        response = self.llm.invoke(messages)

        return {
            "response": response.content,
            "sources": docs,
        }