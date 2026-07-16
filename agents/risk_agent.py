from langchain_core.prompts import ChatPromptTemplate

from agents.base_agent import BaseAgent


class RiskAgent(BaseAgent):

    QUERY = (
        "Project risks, implementation risks, procurement risks, "
        "financial risks, environmental and social risks."
    )

    PROMPT = ChatPromptTemplate.from_template(
        """
You are an experienced World Bank Project Risk Analyst.

Use ONLY the provided project documents.

Analyze the project and produce a structured risk assessment.

Include the following sections:

1. High Risks
2. Medium Risks
3. Low Risks
4. Recommendations

Do not invent risks.

If information is unavailable, explicitly state it.

Context:
{context}
"""
    )

    def analyze_risks(self):
        return self.run()