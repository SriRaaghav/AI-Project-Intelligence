from langchain_core.prompts import ChatPromptTemplate

from rag.llm import get_llm


class ChatAgent:

    def __init__(self):

        self.llm = get_llm()

        self.prompt = ChatPromptTemplate.from_template(
            """
You are an AI Project Intelligence Assistant.

Answer the user's question using ONLY the provided project documents.

Instructions:
- Be accurate and concise.
- Do not hallucinate.
- If the answer is unavailable in the provided context, explicitly say so.
- Quote important figures, dates and project names whenever relevant.

Question:
{question}

Context:
{context}
"""
        )

    def run(self, question: str, documents):

        context = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        messages = self.prompt.format_messages(
            question=question,
            context=context,
        )

        response = self.llm.invoke(messages)

        return response.content