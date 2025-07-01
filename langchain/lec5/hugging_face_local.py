from dotenv import load_dotenv
import os
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

load_dotenv()

hf_api_token = os.getenv("HUGGINGFACE_ACCESS_TOKEN")
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=hf_api_token,
    pipeline_kwargs=dict(
        temperature = 0.5,
        max_new_tokens =100
    )
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of Maharashtra, India?")

print(result)

