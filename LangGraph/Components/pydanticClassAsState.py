from langgraph.graph import StateGraph,START, END
from pydantic import BaseModel

class State(BaseModel):
    a: str

def node_1(state: State) -> State:
    return {"a": "set by node_1"}

builder = StateGraph(State)
builder.add_node("node_1", node_1)
builder.add_edge(START, "node_1")
builder.add_edge("node_1", END)

graph = builder.compile()


print(graph.invoke({"a": "set at start"}))

try:
    graph.invoke({"a":123})
except Exception as e:
    print(f"Error: {e}")
