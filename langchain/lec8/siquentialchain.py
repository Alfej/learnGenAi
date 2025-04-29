from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it",task = "text-generation")

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

tempalate1 = PromptTemplate(
    template= 'give me detailed report on {topic}',
    input_variables=['topic']
)

tempalate2 = PromptTemplate(
    template= 'generate 5 point summary of following text \n {text}',
    input_variables=['text']
)

chain = tempalate1 | model | parser | tempalate2 | model | parser
print(chain.invoke({'topic':"AI"}))

chain.get_graph().print_ascii()
