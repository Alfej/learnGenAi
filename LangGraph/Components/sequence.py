# To add a sequence of nodes, we use the .add_node and .add_edge methods of our graph:
# example:
from langgraph.graph import START, StateGraph

# builder = StateGraph(State)

# # Add nodes
# builder.add_node(step_1)
# builder.add_node(step_2)
# builder.add_node(step_3)

# # Add edges
# builder.add_edge(START, "step_1")
# builder.add_edge("step_1", "step_2")
# builder.add_edge("step_2", "step_3")

# We can also use the built-in shorthand .add_sequence:
# builder = StateGraph(State).add_sequence([step_1, step_2, step_3])
# builder.add_edge(START, "step_1")

# example
from typing_extensions import TypedDict

class State(TypedDict):
    value_1: str
    value_2: int

def step_1(state: State):
    return {"value_1": "a"}

def step_2(state: State):
    current_value_1 = state["value_1"]
    return {"value_1": f"{current_value_1} b"}

def step_3(state: State):
    return {"value_2": 10}

from langgraph.graph import START, StateGraph

builder = StateGraph(State)

# Add nodes
# builder.add_node(step_1)
# builder.add_node(step_2)
# builder.add_node(step_3)

# # Add edges
# builder.add_edge(START, "step_1")
# builder.add_edge("step_1", "step_2")
# builder.add_edge("step_2", "step_3")
# graph = builder.compile()

builder = StateGraph(State).add_sequence([step_1, step_2, step_3])
builder.add_edge(START, "step_1")

graph = builder.compile()

graph.invoke({"value_1": "c"})

print(graph.invoke({"value_1": "c"}))