# Type One using tool decorator

from langchain_community.tools import tool
import json

@tool
def percentage(a: float, b: float) -> float:
    """Calculate the percentage of a over b."""
    return (a / b) * 100

result = percentage.invoke({"b": 200, "a": 50})
# print(result)

# print(percentage.name)
# print(percentage.description)
# print(percentage.args)
# print(json.dumps((percentage.args_schema.model_json_schema())))


# Type Two using StructuredTool in Langchain 

from langchain_community.tools import StructuredTool
from pydantic import BaseModel, Field

class PercentageInput(BaseModel):
    a: float = Field(required=True,description="The part value")
    b: float = Field(description="The total value", required=True)
    
# Get the percentage function from above 

percentage_tool = StructuredTool.from_function(
    func=percentage,
    name="percentage",
    description="Calculate the percentage of a over b.",
    args_schema=PercentageInput
)

result = percentage.invoke({"b": 200, "a": 50})
# print(result)

# type three using base tool class 
from langchain_community.tools import BaseTool
from typing import Type

class percentageInput(BaseModel):
    a: float = Field(required=True, description="The part value")
    b: float = Field(description="The total value", required=True)
    
class PercentageTool(BaseTool):
    name: str = "percentage"
    description: str = "Calculate the percentage of a over b."
    args_schema: Type[BaseModel] = percentageInput
    def _run(self, a: float, b: float) -> float:
        return (a / b) * 100
    
percentage_tool = PercentageTool()
result = percentage_tool.invoke({"b": 200, "a": 50})
print(result)
    