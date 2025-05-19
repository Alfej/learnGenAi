# Adapter is a structural design pattern that allows objects with incompatible interfaces to collaborate.
# An adapter wraps one of the objects to hide the complexity of conversion happening behind the scenes. 
# Applicability:
# Use the Adapter class when you want to use some existing class, but its interface isn’t compatible with the rest of your code.

# In python we can do it with 2 ways:
# 1. By creating a new class that inherits from the class we want to adapt and implementing the methods we need.
# 2. By creating a new class that takes an instance of the class we want to adapt as an argument and implementing the methods we need.

# Example 1:

class Jsontype:
    def _printJson(self,json_message):
        print("Json type",json_message)

class Xmltype:
    def _printXml(self, xml_message):
        print("Xml type",xml_message)
        
class JsonAdapter(Jsontype, Xmltype):
    def __init__(self):
        self.json_message = None
        self.xml_message = None
        
    def _print(self, json_message):
        self.json_message = json_message
        self.xml_message = self.json_message.replace("json", "xml")
        self._printJson(self.json_message)
        self._printXml(self.xml_message)

# JsonObj =  Jsontype()
# JsonObj._printJson("json message")

# xmlObj =  Xmltype()
# xmlObj._printXml("xml message")

# JsonObj = JsonAdapter()
# JsonObj._print("json message")


# Example 2:
class Jsontype:
    def _printJson(self,json_message):
        print("Json type",json_message)

class Xmltype:
    def _printXml(self, xml_message):
        print("Xml type",xml_message)
        
class JsonAdapter(Jsontype):
    def __init__(self, xml_obj):
        self.xml_obj = xml_obj
        
    def _print(self, json_message):
        self.JsonMessage = json_message
        self.xml_message = self.JsonMessage.replace("json", "xml")
        self._printJson(json_message)
        self.xml_obj._printXml(self.xml_message)

JsonObj =  Jsontype()
JsonObj._printJson("json message")

xmlObj =  Xmltype()
xmlObj._printXml("xml message")

JsonObj = JsonAdapter(xmlObj)
JsonObj._print("json message")