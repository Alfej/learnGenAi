from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


load_dotenv()

llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it",task = "text-generation")

model = ChatHuggingFace(llm=llm)

class person(BaseModel):
    name:str = Field(description="Name of the person")
    age:int = Field(gt=18, description="Age of a person")
    city:str = Field(description="Name of the city person lives in")

parser = PydanticOutputParser(pydantic_object=person)

tempalate1 = PromptTemplate(
    template= 'generate a name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={"format_instruction" : parser.get_format_instructions()}
)

chain = tempalate1 | model | parser
print(chain.invoke({'place':"sri lankan"}))
