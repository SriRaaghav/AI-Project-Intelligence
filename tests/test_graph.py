from graph.workflow import graph

state = {
    "question": "Summarize the project",
    "agent": "",
    "response": "",
    "sources": [],
}

result = graph.invoke(state)

print("=" * 80)
print(result["response"])
print("=" * 80)