from __future__ import annotations
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List

class advancementItem(BaseModel):
    technology: str = Field(description="Name of the technology for which advancments are gathered.")
    advancements: str = Field(description="A brief description of the advancements.")
    date: str = Field(description="The date when the advancements were made.")
    impact: str = Field(description="The impact of the advancements on society and technology.")

class advancements(BaseModel):
    items: List[advancementItem] = Field(description="List of advancements in technology.")
    

load_dotenv()

# Tools
search_tool = DuckDuckGoSearchRun()

# LLM
prompt = hub.pull("hwchase17/react")
llm = ChatGroq(model_name='llama3-8b-8192',temperature=0.5)

# Agent
agent = create_react_agent(llm, tools=[search_tool],prompt=prompt)

# Agent Executor
agent_executor = AgentExecutor(agent=agent, tools=[search_tool], verbose=True)

# Run the agent
parser = PydanticOutputParser(pydantic_object=advancements)
advancementPrompt = PromptTemplate(
            template="You are an advancement agent. Your task is to gather recent advancements in the field of {technology}. \n {formate_instructions}",
            input_variables=["technology"],
            partial_variables={"formate_instructions": parser.get_format_instructions()},
        )
chain = advancementPrompt | agent_executor | parser
response = chain.invoke({"technology": "quantum computing"})
print(response)

