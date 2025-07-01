from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

# model = ChatOpenAI(model='gpt-4')

hf_api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation",
    huggingfacehub_api_token=hf_api_token
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of Maharashtra, India?")

print(result)

