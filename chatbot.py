from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(model_name='llama3-8b-8192')

chat_shistory = [SystemMessage(content="You are a helpful assistant.")]

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    
    chat_shistory.append(HumanMessage(content=user_input))
    # Get the model's response
    response = model.invoke(chat_shistory)
    chat_shistory.append(AIMessage(content=response.content))
    print(f"AI: {response.content}")  
    
print(chat_shistory)  