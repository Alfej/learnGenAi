# The State consists of the schema of the graph as well as reducer functions which specify how to apply updates to the state.
# The schema of the State will be the input schema to all Nodes and Edges in the graph, and it can be a TypedDict, Pydantic model, or dataclass
# All Nodes will emit updates to the State which are then applied using the specified reducer function

# schema
#   By default, the graph will have the same input and output schemas. If you want to change this, you can also specify explicit input and output schemas directly
# This is useful when you have a lot of keys, and some are explicitly for input and others for output.

# Reducers:
#  Reducers are key to understanding how updates from nodes are applied to the State.
#  Each key in the State has its own independent reducer function
#  If no reducer function is explicitly specified then it is assumed that all updates to that key should override it.

# Simple State example 
# 2. Made reducer update
    # 2.1 using built-in function as reducer from operator module
    # 2.2 using custom reducer function
    # 2.3 using built-in function as reducer from langgraph.graph.message module
# 3. multiple states 

from langchain_core.messages import AnyMessage, AIMessage
from typing_extensions import TypedDict
from langgraph.graph import StateGraph
from IPython.display import Image, display
from typing import Annotated
from langgraph.graph.message import add_messages #2.3 another reducer function that can be used to update a list of messages
# from operator import add #2.1 this is a built-in function that can be used as a reducer

# 2.2 custom reducer function
def add(a: list[AnyMessage], b: [AnyMessage]) -> list[AnyMessage]:
    a.extend(b)
    return a
class State(TypedDict):
    # messages: list[AnyMessage] # No reducer function is specified
    # messages: Annotated[list[AnyMessage], add_messages] # Uncomment for 2.1
    # messages: Annotated[list[AnyMessage], add]  # Uncomment for 2.2
    messages: Annotated[list[AnyMessage], add_messages] # 2.3 using built-in function as reducer from langgraph.graph.message module
    extra_field: int

# This state tracks a list of message objects, as well as an extra integer field.
# Update state
# Let's build an example graph with a single node. Our node is just a Python function that reads our graph's state and makes updates to it. The first argument to this function will always be the state:

# Single State example
def my_node(state: State) -> State:
    # messages = state["messages"] # uncomment for 1 simple state example
    new_message = AIMessage(content="Hello, world!")
    # messages.append(new_message)  # uncomment for 1 simple state example, No need to use append, as we are using a reducer function that will handle the update

    return {"messages": [new_message], "extra_field": 10}

graph = StateGraph(State)
graph.add_node("node", my_node)
graph.set_entry_point("node")
L_graph = graph.compile()


display(Image(L_graph.get_graph().draw_mermaid_png()))
result = L_graph.invoke({"messages": [], "extra_field": 0})
print(result)

for message in result["messages"]:
    message.pretty_print()