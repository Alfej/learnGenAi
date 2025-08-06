# There are many use cases where you may wish for your node to have a custom retry policy, for example if you are calling an API, querying a database, or calling an LLM, etc. LangGraph lets you add retry policies to nodes.
# To configure a retry policy, pass the retry_policy parameter to the add_node. The retry_policy parameter takes in a RetryPolicy named tuple object. Below we instantiate a RetryPolicy object with the default parameters and associate it with a node:

# By default, the retry_on parameter uses the default_retry_on function, which retries on any exception except for the following:

# ValueError
# TypeError
# ArithmeticError
# ImportError
# LookupError
# NameError
# SyntaxError
# RuntimeError
# ReferenceError
# StopIteration
# StopAsyncIteration
# OSError


from langgraph.pregel import RetryPolicy
from langgraph.graph import StateGraph, MessagesState

builder = StateGraph(MessagesState)
def node_function():
    print("In Node")

builder.add_node(
    "node_name",
    node_function,
    retry_policy=RetryPolicy()
)


# Cache Policy
# Node caching is useful in cases where you want to avoid repeating operations, like when doing something expensive (either in terms of time or cost). LangGraph lets you add individualized caching policies to nodes in a graph.

# To configure a cache policy, pass the cache_policy parameter to the add_node function. In the following example, a CachePolicy object is instantiated with a time to live of 120 seconds and the default key_func generator. Then it is associated with a node:

from langgraph.types import CachePolicy

builder.add_node(
    "node_name",
    node_function,
    cache_policy=CachePolicy(ttl=120),
)
# Then, to enable node-level caching for a graph, set the cache argument when compiling the graph. The example below uses InMemoryCache to set up a graph with in-memory cache, but SqliteCache is also available.

from langgraph.cache.memory import InMemoryCache

graph = builder.compile(cache=InMemoryCache())