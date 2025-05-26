from langchain_groq import ChatGroq
from langchain_core.tools import tool,InjectedToolArg
from langchain_core.messages import HumanMessage
from typing import Annotated
import requests
import json
from dotenv import load_dotenv

load_dotenv()

@tool
def get_conversion_rate(base_currency: str, target_currency: str) -> float:
    """Function fetches the currecy conversion factor beetween a given base currency and a target currency."""
    url = f"https://v6.exchangerate-api.com/v6/17e89dfa93d1d93ec234bcb8/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    data = response.json()
    return data

@tool
def convert(base_currency_amount: int, conversion_rate: Annotated[float, InjectedToolArg]) -> float:
    """Function converts a given base currency amount to a target currency using the conversion rate."""
    return base_currency_amount * conversion_rate


messages = [HumanMessage("can you convert 10 EUR to USD?")]
model = ChatGroq(model_name='llama3-8b-8192',temperature=0.4)
llm_with_tools = model.bind_tools([get_conversion_rate, convert])
response = llm_with_tools.invoke(messages)
messages.append(response)
# print(response.tool_calls)

for tool_call in response.tool_calls:
    if tool_call['name'] == "get_conversion_rate":
        conversion_rate = get_conversion_rate.invoke(tool_call)
        messages.append(conversion_rate)
        conversion_rate = json.loads(conversion_rate.content)['conversion_rate']
        
        
    elif tool_call['name'] == "convert":
        tool_call['args']['conversion_rate'] = conversion_rate
        converted_amount = convert.invoke(tool_call)
        messages.append(converted_amount)

print(messages)      

response = llm_with_tools.invoke(messages)
messages.append(response)
print(response)