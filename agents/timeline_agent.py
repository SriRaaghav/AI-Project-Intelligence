from langchain_core.prompts import ChatPromptTemplate

from agents.base_agent import BaseAgent


class TimelineAgent(BaseAgent):

    QUERY = (
        "Project timeline, milestones, approval date, "
        "implementation schedule, closing date."
    )

    PROMPT = ChatPromptTemplate.from_template(
        """
You are an AI Project Intelligence Assistant.

Use ONLY the provided project documents.

Extract the project timeline.

Include the following sections:

1. Approval Date
2. Effectiveness Date
3. Closing Date
4. Major Milestones
5. Current Project Status

If information is unavailable, explicitly state it.

Present the output in a clear chronological format.

Context:
{context}
"""
    )

    def extract_timeline(self):
        return self.run()