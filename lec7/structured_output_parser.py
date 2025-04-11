from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate, MessagesPlaceholder
from langchain.output_parsers import StructuredOutputParser, ResponseSchema


load_dotenv()

llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it",task = "text-generation")

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name="fact_1",description="first genarated fact about topic"),
    ResponseSchema(name="fact_2",description="second genarated fact about topic"),
    ResponseSchema(name="fact_3",description="Third genarated fact about topic")
]

parser = StructuredOutputParser.from_response_schemas(schema)

tempalate1 = PromptTemplate(
    template= 'give me 3 facts about {topic}\n {format_instruction}',
    input_variables=['topic'],
    partial_variables={"format_instruction" : parser.get_format_instructions()}
)

# prompt = tempalate1.invoke({'topic':'AI'})
# response = model.invoke(prompt)

chain = tempalate1 | model | parser

print(chain.invoke({'topic':"Ai"}))