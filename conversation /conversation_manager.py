from graph.chat.chat_workflow import chat_graph

from graph.summary.workflow import summary_graph
from graph.risk.risk_workflow import risk_graph
from graph.timeline.workflow import timeline_graph
from graph.procurement.workflow import procurement_graph
from graph.health.workflow import health_graph


class ConversationManager:

    def handle_chat(self, question: str):

        state = {
            "question": question,
            "documents": [],
            "response": "",
        }

        result = chat_graph.invoke(state)

        return result["response"]


    def handle_summary(self):

        state = {
            "question": "Generate Executive Summary",
            "documents": [],
            "summary": None,
        }

        result = summary_graph.invoke(state)

        return result["summary"]


    def handle_risk(self):

        state = {
            "question": "Generate Risk Analysis",
            "documents": [],
            "risk": None,
        }

        result = risk_graph.invoke(state)

        return result["risk"]


    def handle_timeline(self):

        state = {
            "question": "Generate Timeline Analysis",
            "documents": [],
            "timeline": None,
        }

        result = timeline_graph.invoke(state)

        return result["timeline"]


    def handle_procurement(self):

        state = {
            "question": "Generate Procurement Analysis",
            "documents": [],
            "procurement": None,
        }

        result = procurement_graph.invoke(state)

        return result["procurement"]


    def handle_health(self):

        state = {
            "question": "Generate AI Project Health Report",
            "documents": [],
            "summary": None,
            "risk": None,
            "timeline": None,
            "procurement": None,
            "health_score": None,
        }

        result = health_graph.invoke(state)

        return result["health_score"]