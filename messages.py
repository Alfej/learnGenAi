from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model_name='llama3-8b-8192')

messages = [SystemMessage(content="You are a helpful assistant."),
           HumanMessage(content="What is the capital of France?")]

model_response = model.invoke(messages)
messages.append(AIMessage(content=model_response.content))
print(messages)    
