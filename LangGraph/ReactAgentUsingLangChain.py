from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from langchain.agents import initialize_agent
from langchain_community.tools import DuckDuckGoSearchResults

load_dotenv("/.env")

search_tool = DuckDuckGoSearchResults()

model = ChatGroq(model_name='llama3-8b-8192',temperature=0.4)

Agent = initialize_agent(tools=[search_tool], llm=model, agent="zero-shot-react-description", verbose = True )
Agent.invoke("How many days ago the latest spaceX launch has happened?")

# response = model.invoke("GIve me todays wheather information in banglore")

# print(response)