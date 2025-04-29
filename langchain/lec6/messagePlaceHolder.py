from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model_name='llama3-8b-8192')

Chat_template = ChatPromptTemplate(
    [
        ('system', "You are a helpful customer support expert."),
        MessagesPlaceholder(variable_name="chat_history"),
        ('human', "{query}")
    ]
)

chat_history = [
    HumanMessage(content="What is the status of my refund?"),
    AIMessage(content="Your refund is being processed and should be completed within 5-7 business days.")
] 

prompt = Chat_template.invoke({'chat_history': chat_history, 'query': 'Can you provide an update on my order status?'})

print(prompt)  # This will print the formatted prompt