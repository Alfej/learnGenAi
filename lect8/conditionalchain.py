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

model = ChatGroq(model_name='llama3-8b-8192')

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


# parser = StrOutputParser()

# class Feedback(BaseModel):

#     sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

# parser2 = PydanticOutputParser(pydantic_object=Feedback)

# prompt1 = PromptTemplate(
#     template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
#     input_variables=['feedback'],
#     partial_variables={'format_instruction':parser2.get_format_instructions()}
# )

# classifier_chain = prompt1 | model | parser2

# prompt2 = PromptTemplate(
#     template='Write an appropriate response to this positive feedback \n {feedback}',
#     input_variables=['feedback']
# )

# prompt3 = PromptTemplate(
#     template='Write an appropriate response to this negative feedback \n {feedback}',
#     input_variables=['feedback']
# )

# branch_chain = RunnableBranch(
#     (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
#     (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
#     RunnableLambda(lambda x: "could not find sentiment")
# )

# chain = classifier_chain | branch_chain

# print(chain.invoke({'feedback': 'This is a beautiful phone'}))

# chain.get_graph().print_ascii()