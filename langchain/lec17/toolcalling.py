from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests
from dotenv import load_dotenv

load_dotenv()

@tool
def percentage(a: float, b: float) -> float:
    """Calculate the percentage of a over b."""
    return (a / b) * 100

model = ChatGroq(model_name='llama3-8b-8192',temperature=1)
llm_with_tools = model.bind_tools([percentage])

query = HumanMessage("Can you find 20 is what percentage of 50?")
messages = [query]
response = llm_with_tools.invoke(messages) 
messages.append(response)# This will call the percentage tool

print(response)
print(response.tool_calls)  # This will print the tool that was called
tool_message = percentage.invoke(response.tool_calls[0])# This will print the tool that was called

messages.append(tool_message)
print(messages)  # This will print the tool that was called
print(llm_with_tools.invoke(messages))
