from agents.summary_agent import SummaryAgent
from agents.risk_agent import RiskAgent
from agents.timeline_agent import TimelineAgent
from agents.procurement_agent import ProcurementAgent

from agents.router_prompt import ROUTER_PROMPT

from rag.llm import get_llm


llm = get_llm()

summary_agent = SummaryAgent()
risk_agent = RiskAgent()
timeline_agent = TimelineAgent()
procurement_agent = ProcurementAgent()


def router_node(state):

    messages = ROUTER_PROMPT.format_messages(
        question=state["question"]
    )

    response = llm.invoke(messages)

    agent = response.content.strip().lower()

    valid_agents = {
        "summary",
        "risk",
        "timeline",
        "procurement",
    }

    if agent not in valid_agents:
        agent = "summary"

    state["agent"] = agent

    return state


def summary_node(state):

    result = summary_agent.generate_summary()

    state["response"] = result["response"]
    state["sources"] = result["sources"]

    return state


def risk_node(state):

    result = risk_agent.analyze_risks()

    state["response"] = result["response"]
    state["sources"] = result["sources"]

    return state


def timeline_node(state):

    result = timeline_agent.extract_timeline()

    state["response"] = result["response"]
    state["sources"] = result["sources"]

    return state


def procurement_node(state):

    result = procurement_agent.analyze_procurement()

    state["response"] = result["response"]
    state["sources"] = result["sources"]

    return state