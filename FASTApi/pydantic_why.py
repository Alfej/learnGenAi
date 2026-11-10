#  Suppose we are writing a function to enter the data in database 

# def inser_data(name, age):

#     # For now assume  the below print statement is inserting the data in database
#     print(f"Inserting data into database: Name: {name}, Age: {age}")


# # Another dev uses above function as below
# inser_data("John Doe", "Thirty")  # This will insert the data into the database

# #  fisrt fix assign data type to the age parameter in the function definition

# def inser_data(name : str, age : int):

#     # For now assume  the below print statement is inserting the data in database
#     print(f"Inserting data into database: Name: {name}, Age: {age}")


# # Another dev uses above function as below
# inser_data("John Doe", "Thirty")  # This will insert the data into the database it will not enforce the data type of age parameter to be int. It will still accept string value for age parameter.

# Solution
# def inser_data(name : str, age : int):

#     if type(age) == int and type(name) is str:
#         print(f"Inserting data into database: Name: {name}, Age: {age}")
#     else:
#         raise ValueError("Age must be an integer and Name must be a string")


# # Another dev uses above function as below
# inser_data("John Doe", "Thirty")  # This will insert the data into the database it will not enforce the data type of age parameter to be int. It will still accept string value for age parameter.

#  this is a simple example of how we can enforce the data type of parameters in a function using python. But this is not a good way to enforce the data type of parameters in a function. Because we have to write the code to check the data type of each parameter in the function. This will make the code messy and hard to read.

#  Another issue is what if we want to have a validation check for the parameters. For example, we want to check if the age is greater than 0. We have to write the code to check the validation for each parameter in the function. This will make the code messy and hard to read.

#  pydantic works in the below 3 parts
# 1. define a pydantic model that represents the ideal schema of the data we want to accept in the function. The pydantic model will have the data type and validation checks for each parameter in the function.
# 2. instantiate the pydantic model with the data we want to accept in the function. The pydantic model will validate the data and raise an error if the data is not valid.
# 3. use the validated data from the pydantic model in the function.

from pydantic import BaseModel,EmailStr, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(..., description="Name of the patient", json_schema_extra={"example": ["John Doe", "Jane Doe"]}, min_length=1, max_length=50)]
    age: int = Field(..., gt=0, description="Age must be greater than 0")
    email: Annotated[Optional[EmailStr], Field(None, description="Email address of the patient")] = None
    weight: float = Field(None, gt=0, description="Weight must be greater than 0")
    height: float = Field(None, gt=0, description="Height must be greater than 0")
    marital_status: Annotated[bool, Field(default=False, description="Marital status of the patient", json_schema_extra={"example": True})]
    allergies: Optional[List[str]] = []
    contacts: Dict[str, str] = {}

def inser_data(patient: Patient):

    # For now assume  the below print statement is inserting the data in database
    print(f"Inserting data into database: Name: {patient.name}, Age: {patient.age}, Weight: {patient.weight}, Height: {patient.height}, Marital Status: {patient.marital_status}, Allergies: {patient.allergies}, Contacts: {patient.contacts}")

patient_data = {"name":"John Doe", "age":"30",  "height":175.0, "marital_status":True, "allergies":["Peanuts"], "contacts":{"email":"john.doe@example.com", "phone":"123-456-7890"}}  # This will validate the data and raise an error if the data is not valid.

patient1 = Patient(**patient_data)  # This will validate the data and raise an error if the data is not valid.

inser_data(patient1)  # This will insert the data into the database