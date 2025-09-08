# Visitor is a behavioral design pattern that lets you separate algorithms from the objects on which they operate.

# Applicability
#  Use the Visitor when you need to perform an operation on all elements of a complex object structure (for example, an object tree).
#  Use the Visitor to clean up the business logic of auxiliary behaviors.
#  Use the pattern when a behavior makes sense only in some classes of a class hierarchy, but not in others.

from __future__ import annotations
from abc import ABC,abstractmethod
class HTMLPage:
    def __init__(self):
        self.objs = []

    def add(self, obj:component):
        self.objs.append(obj)

    def printXMl(self,v:visitor):
        for obj in self.objs:
            obj.accept(v)

class component(ABC):
    
    @abstractmethod
    def accept(self, v:visitor):
        pass

class textInput(component):
    def __init__(self):
        self.val = input("Please enter value: ")

    def accept(self, v):
        return v.export_text_information(self)
    
class DropDownInput(component):
    def __init__(self):
        self.type = input("Please enter type: ")

    def accept(self, v):
        return v.export_DropDown_information(self)
    
class visitor(ABC):
    @abstractmethod
    def export_text_information(self, obj:textInput):
        pass

    @abstractmethod
    def export_DropDown_information(self, obj:DropDownInput):
        pass


class ExportXMl(visitor):
    def export_text_information(self, obj:textInput):
        print("XML Representation of a TextInput element")
        print(f"Value: {obj.val}")

    def export_DropDown_information(self, obj:DropDownInput):
        print("XML Representation of a DropDown element")
        print(f"Type: {obj.type}")


if __name__=="__main__":
    html = HTMLPage()
    html.add(textInput())
    html.add(DropDownInput())
    html.add(DropDownInput())
    html.add(textInput())


    v = ExportXMl()
    html.printXMl(v)
    
