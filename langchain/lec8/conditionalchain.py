from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import PydanticOutputParser,StrOutputParser
from pydantic import BaseModel,Field
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from typing import Literal

load_dotenv()

# llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it",task = "text-generation")

# model = ChatHuggingFace(llm=llm)

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

parser1 = StrOutputParser()

class sentiment_analysis(BaseModel):
    sentiment:Literal['Positive','Negative'] = Field(description="give the Sentiment of the feedback")

parser2 =  PydanticOutputParser(pydantic_object=sentiment_analysis)

tempalate2 = PromptTemplate(
    template= 'classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}

)

sentiment_analysis_chain = tempalate2 | model | parser2

tempalate3 = PromptTemplate(
    template= 'Write an appropriate response for this positive feedback \n {feedback}',
    input_variables=['feedback']
)

tempalate4 = PromptTemplate(
    template= 'Write an appropriate response for this negative feedback \n {feedback}',
    input_variables=['feedback']
)

brach_chain = RunnableBranch(
    (lambda x:x.sentiment == 'Positive', tempalate3 | model | parser1),
    (lambda x:x.sentiment == 'Negative', tempalate4 | model | parser1),
    RunnableLambda(lambda x: "Could not find sentiment" )
)

chain = sentiment_analysis_chain | brach_chain

print(chain.invoke({'feedback': 'This is a beautiful phone'}))