from typing import TypedDict
from typing_extensions import Annotated
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(model_name='llama3-8b-8192')

class review (TypedDict):
    summary: str
    sentiment: Annotated[str,...,"values from 'positive', 'negative', 'neutral' based on the sentiment of the review"]

structed_model = model.with_structured_output(review)

result = structed_model.invoke("NO one taught this concept on youtube with this much clarity you are the best teacher i have got thank you is not enough but whatever knowledge i have about ai and ml its only because of you ! stay always blissful")

print(result)  # This will print the dictionary with the specified keys and types

 # This will print the dictionary with the specified keys and types