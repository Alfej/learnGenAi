from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it",task = "text-generation")

model = ChatHuggingFace(llm=llm)

# model = ChatGroq(model_name='llama3-8b-8192')


# first prompt
prompt1 = PromptTemplate(
    input_variables=["topic"],
    template="Write a detiled report about the {topic}"
)

# second prompt
prompt2 = PromptTemplate(
    input_variables=["text"],
    template="Write a five line summary from the following text.\n {text}"
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "AI"})
print(result)  # This will print the formatted prompt