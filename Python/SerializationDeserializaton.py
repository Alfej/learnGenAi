# Serialization: Process of converting python datatype to JSON
# Deserialization: Process of converting JSON to python datatype

#  Serialization
import json
list1 = [1, 2, 3, 4, 5]

with open("Python/data.json", "w") as f:
    json.dump(list1, f)

Dictionary1 = {"name": "John", "age": 30, "city": "New York"}
with open("Python/data.json", "w") as f:
    json.dump(Dictionary1, f,indent=4)

#  Deserialization
with open("Python/data.json", "r") as f:
    data = json.load(f)
    print(type(data))
    print(data)

#  Storing a tuple in JSON format will convert it to a list


#  Serialize custom objects

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person = Person("John", 30)

def person_serializer(obj):
    if isinstance(obj, Person):
        return {"name": obj.name, "age": obj.age}
    raise TypeError("Type not serializable")

with open("Python/data.json", "w") as f:
    json.dump(person, f,default=person_serializer, indent=4)

#  When we will load the data we will get a dictionary instead of a Person object. To convert it back to a Person object, we can use the following code:
def person_deserializer(dct):
    if "name" in dct and "age" in dct:
        return Person(dct["name"], dct["age"])
    return dct

with open("Python/data.json", "r") as f:
    data = json.load(f, object_hook=person_deserializer)
    print(type(data))

#  Pickling 
#  Pickling is the process of converting a Python object into a byte stream, and unpickling is the process of converting a byte stream back into a Python object. The `pickle` module in Python provides this functionality.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

p = Person("John", 30)

import pickle

# Serialize the object
with open("Python/person.pkl", "wb") as f:
    pickle.dump(p, f)

# Deserialize the object
with open("Python/person.pkl", "rb") as f:
    p_loaded = pickle.load(f)
    p_loaded.display()