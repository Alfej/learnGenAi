from dotenv import load_dotenv
import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

hf_api_token = os.getenv("HUGGINGFACE_ACCESS_TOKEN")
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=hf_api_token
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of Maharashtra, India?")

print(result)

