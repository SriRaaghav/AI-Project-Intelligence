from graph.chat.chat_agent import ChatAgent
from rag.retriever import retrieve_context


def retrieve_node(state):

    documents = retrieve_context(
        query=state["question"],
        k=10,
    )

    state["documents"] = documents

    return state


def chat_node(state):

    agent = ChatAgent()

    response = agent.run(
        question=state["question"],
        documents=state["documents"],
    )

    state["response"] = response

    return state