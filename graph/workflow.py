from langgraph.graph import END
from langgraph.graph import START
from langgraph.graph import StateGraph

from graph.state import GraphState
from graph.nodes import (
    router_node,
    summary_node,
    risk_node,
    timeline_node,
    procurement_node,
)


workflow = StateGraph(GraphState)

# Nodes
workflow.add_node("router", router_node)
workflow.add_node("summary", summary_node)
workflow.add_node("risk", risk_node)
workflow.add_node("timeline", timeline_node)
workflow.add_node("procurement", procurement_node)

# Start
workflow.add_edge(START, "router")


# Routing Function
def decide_next_node(state):

    return state["agent"]


# Conditional Routing
workflow.add_conditional_edges(
    "router",
    decide_next_node,
    {
        "summary": "summary",
        "risk": "risk",
        "timeline": "timeline",
        "procurement": "procurement",
    },
)

# End
workflow.add_edge("summary", END)
workflow.add_edge("risk", END)
workflow.add_edge("timeline", END)
workflow.add_edge("procurement", END)


graph = workflow.compile()