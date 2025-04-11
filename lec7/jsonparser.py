from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()

llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it",task = "text-generation")

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

tempalate1 = PromptTemplate(
    template= 'give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={"format_instruction" : parser.get_format_instructions()}
)

chain = tempalate1 | model | parser
print(chain.invoke({'topic':"AI"}))
