# Sometimes you want to be able to configure your graph when calling it. For example, you might want to be able to specify what LLM or system prompt to use at runtime, without polluting the graph state with these parameters.

# Specify a schema for your configuration
# Add the configuration to the function signature for nodes or conditional edges
# Pass the configuration into the graph.

from langchain_core.runnables import RunnableConfig
from langgraph.graph import END, StateGraph, START
from typing_extensions import TypedDict

# 1. Specify config schema
class ConfigSchema(TypedDict):
    my_runtime_value: str

# 2. Define a graph that accesses the config in a node
class State(TypedDict):
    my_state_value: str

def node(state: State, config: RunnableConfig):
    if config["configurable"]["my_runtime_value"] == "a":
        return {"my_state_value": 1}
    elif config["configurable"]["my_runtime_value"] == "b":
        return {"my_state_value": 2}
    else:
        raise ValueError("Unknown values.")

builder = StateGraph(State, config_schema=ConfigSchema)
builder.add_node(node)
builder.add_edge(START, "node")
builder.add_edge("node", END)

graph = builder.compile()

# 3. Pass in configuration at runtime:
print(graph.invoke({}, {"configurable": {"my_runtime_value": "a"}}))
print(graph.invoke({}, {"configurable": {"my_runtime_value": "b"}}))