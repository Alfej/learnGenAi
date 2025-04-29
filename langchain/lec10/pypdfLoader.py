from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it",task = "text-generation")

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

tempalate1 = PromptTemplate(
    template= 'Can you Name the candidate and its information like what is the company he/her working in and what is the tech stack and what is the role offerd right now from a given content?. {content}',
    input_variables=['content']
)

loader = PyPDFLoader("lec10/19BCE130_PPR.pdf")

docs = loader.load()

# print(docs)
# print(type(docs))
# print(len(docs))

# print(docs[0])

# print(docs[0].metadata)

chain = tempalate1 | model | parser
print(chain.invoke({'content':docs[0].page_content}))