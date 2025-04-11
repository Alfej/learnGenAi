from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_groq import ChatGroq

from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model_name='llama3-8b-8192')

chat_template = ChatPromptTemplate(
    [
    ('system', "You are a helpful {domain} expert."),
    ('human', "explain {topic} in simple terms."),
    ]
)

prompt = chat_template.invoke({'domain': 'AI', 'topic': 'prompt engineering'})
print(prompt)  # This will print the formatted prompt
