from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it",task = "text-generation")

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

tempalate1 = PromptTemplate(
    template= 'give me detailed report on {topic}',
    input_variables=['topic']
)

tempalate2 = PromptTemplate(
    template= 'generate a short and simple notes from the following text \n {text}',
    input_variables=['text']
)

tempalate3 = PromptTemplate(
    template= 'generate a 5 short questions from the following text \n {text}',
    input_variables=['text']
)

tempalate4 = PromptTemplate(
    template= 'merge notes and queiz into a single document \n notes -> {notes} \n quizes-> {quize}',
    input_variables=['notes','quize']
)

parallechain = RunnableParallel(
    {
        'notes': tempalate2 | model | parser,
        'quize': tempalate3 | model | parser
    }
)

start_chain = tempalate1 | model | parser
merge_chain = tempalate4 | model | parser

chain = start_chain | parallechain | merge_chain

result = chain.invoke({'topic': "Generative AI"})

print(result)
chain.get_graph().print_ascii()