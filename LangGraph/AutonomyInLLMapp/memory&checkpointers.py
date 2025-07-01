"""
Memory & Checkpointers
When you build a basic chatbot using LangGraph, you run into an immediate limitation: by default, your chatbot has amnesia.
Every time a user starts a conversation, the bot has no recollection of previous interactions.
This happens because without memory management, each invocation of your graph is completely independent.
This is where the concept of checkpointers in LangGraph come into the picture

Whqt is q Checkpointer?
A checkpointer in LangGraph is essentially a way to save the state of your agent or workflow at specific points during execution.
Think of it like saving your progress in a video game. When you reach a checkpoint:
    1. The current state of everything is saved
    2. If something goes wrong later, you can return to this saved point
    3. You don't have to start over from the beginning

In the context of LangGraph nodes and workflows:
    • Nodes are the individual steps or components in your workflow
    • Checkpoints save the complete state after a node finishes its work
    • If an error occurs in a later node, you can resume from the last checkpoint rather than starting the entire workflow again

This is particularly useful for complex workflows where:
    • Processing takes significant time or resources
    • You want to implement retry mechanisms
    • You need persistence across sessions or server restarts


Thread ID:
A thread ID is simply a unique identifier for each specific conversation or workflow execution. Think of it like:
    - A unique session ID for a user
    - A conversation ID that groups related messages together
The thread ID is necessary because:
1. You might have multiple conversations/workflows running simultaneously
2. Each needs its own separate saved state
3. The thread ID helps the system know which saved state belongs to which conversation
Without thread IDs, all your conversations would share the same state, which would causel confusion and errors.
"""
