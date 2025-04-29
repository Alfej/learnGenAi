from langchain_community.document_loaders import TextLoader
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
    template= 'What is company name candidate worked in?. {content}',
    input_variables=['content']
)

loader = TextLoader("lec10/myInformation.txt")

docs = loader.load()

# print(type(docs))
# print(len(docs))

# print(docs[0])

# print(docs[0].metadata)

chain = tempalate1 | model | parser
print(chain.invoke({'content':docs[0].page_content}))