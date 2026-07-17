from langchain_core.prompts import ChatPromptTemplate

ROUTER_PROMPT = ChatPromptTemplate.from_template(
"""
You are an AI Router.

Choose the SINGLE most appropriate specialist.

Available specialists:

summary
risk
timeline
procurement

Rules:

- Return ONLY one of the four words above.
- Do NOT explain your choice.
- Do NOT use punctuation.
- Do NOT return a sentence.

Question:
{question}
"""
)