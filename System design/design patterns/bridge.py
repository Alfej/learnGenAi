# Bridge is a structural design pattern that lets you split a large class or a set of closely related classes into two separate hierarchies—abstraction and implementation—which can be developed independently of each other.

# Problem: 
# Say you have a geometric Shape class with a pair of subclasses: Circle and Square. You want to extend this class hierarchy to incorporate colors, so you plan to create Red and Blue shape subclasses. However, since you already have two subclasses, you’ll need to create four class combinations such as BlueCircle and RedSquare.Adding new shape types and colors to the hierarchy will grow it exponentially. For example, to add a triangle shape you’d need to introduce two subclasses, one for each color. And after that, adding a new color would require creating three subclasses, one for each shape type. The further we go, the worse it becomes.

# Solution:
# This problem occurs because we’re trying to extend the shape classes in two independent dimensions: by form and by color. That’s a very common issue with class inheritance.
# The Bridge pattern attempts to solve this problem by switching from inheritance to the object composition. What this means is that you extract one of the dimensions into a separate class hierarchy, so that the original classes will reference an object of the new hierarchy, instead of having all of its state and behaviors within one class.
# Following this approach, we can extract the color-related code into its own class with two subclasses: Red and Blue. The Shape class then gets a reference field pointing to one of the color objects. Now the shape can delegate any color-related work to the linked color object. That reference will act as a bridge between the Shape and Color classes. From now on, adding new colors won’t require changing the shape hierarchy, and vice versa.

# Applicability:
#  Use the Bridge pattern when you want to divide and organize a monolithic class that has several variants of some functionality (for example, if the class can work with various database servers)
# Use the pattern when you need to extend a class in several orthogonal (independent) dimensions.
# Use the Bridge if you need to be able to switch implementations at runtime.

from __future__ import annotations
from abc import ABC, abstractmethod


# class Abstraction:
#     """
#     The Abstraction defines the interface for the "control" part of the two
#     class hierarchies. It maintains a reference to an object of the
#     Implementation hierarchy and delegates all of the real work to this object.
#     """

#     def __init__(self, implementation: Implementation) -> None:
#         self.implementation = implementation

#     def operation(self) -> str:
#         return (f"Abstraction: Base operation with:\n"
#                 f"{self.implementation.operation_implementation()}")


# class ExtendedAbstraction(Abstraction):
#     """
#     You can extend the Abstraction without changing the Implementation classes.
#     """

#     def operation(self) -> str:
#         return (f"ExtendedAbstraction: Extended operation with:\n"
#                 f"{self.implementation.operation_implementation()}")


# class Implementation(ABC):
#     """
#     The Implementation defines the interface for all implementation classes. It
#     doesn't have to match the Abstraction's interface. In fact, the two
#     interfaces can be entirely different. Typically the Implementation interface
#     provides only primitive operations, while the Abstraction defines higher-
#     level operations based on those primitives.
#     """

#     @abstractmethod
#     def operation_implementation(self) -> str:
#         pass


# """
# Each Concrete Implementation corresponds to a specific platform and implements
# the Implementation interface using that platform's API.
# """


# class ConcreteImplementationA(Implementation):
#     def operation_implementation(self) -> str:
#         return "ConcreteImplementationA: Here's the result on the platform A."


# class ConcreteImplementationB(Implementation):
#     def operation_implementation(self) -> str:
#         return "ConcreteImplementationB: Here's the result on the platform B."


# def client_code(abstraction: Abstraction) -> None:
#     """
#     Except for the initialization phase, where an Abstraction object gets linked
#     with a specific Implementation object, the client code should only depend on
#     the Abstraction class. This way the client code can support any abstraction-
#     implementation combination.
#     """

#     # ...

#     print(abstraction.operation(), end="")

#     # ...


# if __name__ == "__main__":
#     """
#     The client code should be able to work with any pre-configured abstraction-
#     implementation combination.
#     """

#     implementation = ConcreteImplementationA()
#     abstraction = Abstraction(implementation)
#     client_code(abstraction)

#     print("\n")

#     implementation = ConcreteImplementationB()
#     abstraction = ExtendedAbstraction(implementation)
#     client_code(abstraction)
    
    

class Shape(ABC):
    def __init__(self, color: Color) -> None:
        self.color = color
    
    @abstractmethod
    def draw(self) -> str:
        pass
    
    def getColor(self) -> str:
        return self.color.fill_color()

class Circle(Shape):
    def draw(self) -> str:
        return f"Circle with color: {self.getColor()}"
    
class Square(Shape):
    def draw(self) -> str:
        return f"Square with color: {self.getColor()}"
    
class Color(ABC):
    @abstractmethod
    def fill_color(self) -> str:
        pass
    
class Red(Color):
    def fill_color(self) -> str:
        return "Red"

class Blue(Color):
    def fill_color(self) -> str:
        return "Blue"
    
def client_code_shape(shape: Shape) -> None:
    """
    The client code should be able to work with any pre-configured shape-color
    combination.
    """
    print(shape.draw())
    
if __name__ == "__main__":
    """
    The client code should be able to work with any pre-configured shape-color
    combination.
    """
    
    red_circle = Circle(Red())
    client_code_shape(red_circle)
    
    blue_square = Square(Blue())
    client_code_shape(blue_square)
    
    red_square = Square(Red())
    client_code_shape(red_square)
    
    blue_circle = Circle(Blue())
    client_code_shape(blue_circle)
    
    