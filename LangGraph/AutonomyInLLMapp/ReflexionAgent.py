"""
Reflection Agent System consists of a generator and a reflector component

Although, iteratively making a post better is significantly better than just
prompting ChatGPT, the content generated is still not grounded in live data

It could be hallucination or outdated content and we have no way of knowing

Reflexion Agent addresses this drwback 

The reflexion agent, similar to reflection agent, not only critiques it's own
responses but also fact checks it with external data by making API calls (Internet
Search)

The main component of Reflexion Agent System is the "actor"

The "actor" is the main agent that drives everything - it reflects on it's responses
and re-executes.

It can do this with or without tools to improve based on self-critique that is
grounded in external data

It's main sub-components include:
I. Tools/tool execution
2. Initial responder: generate an initial response & self-reflection
3. Revisor: re-respond & reflect based on previous reflections

In the context of Reflexion agents, episodic memory refers to an agent's ability
to recall specific past interactions, events, or experiences, rather than just
generalized knowledge.
This is crucial for making agents feel more context-aware, personalized, and
human-like over time.
"""