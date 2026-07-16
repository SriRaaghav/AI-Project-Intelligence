from langchain_core.prompts import ChatPromptTemplate

from agents.base_agent import BaseAgent


class ProcurementAgent(BaseAgent):

    QUERY = (
        "Procurement arrangements, procurement methods, "
        "implementing agency, contracts, governance."
    )

    PROMPT = ChatPromptTemplate.from_template(
        """
You are an AI Procurement Specialist for World Bank projects.

Use ONLY the provided project documents.

Generate a procurement analysis.

Include:

1. Procurement Methods
2. Implementing Agencies
3. Major Contracts
4. Procurement Risks
5. Governance Recommendations

If information is unavailable, explicitly state it.

Context:
{context}
"""
    )

    def analyze_procurement(self):
        return self.run()