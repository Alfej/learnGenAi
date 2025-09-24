# interface Segregation Principle (ISP):
#     Many client-specific interfaces are better than one general-purpose interface.
#     Clients should not be forced to depend on interfaces they do not use.

# ex: Violation of ISP
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def volume(self):
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def volume(self):
        raise NotImplementedError("Circle does not have volume")

class Cube(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self):
        return 6 * self.side * self.side

    def volume(self):
        return self.side * self.side * self.side
    
# In this example, the Circle class is forced to implement the volume method, which it does not need. This violates the ISP.
# To adhere to ISP, we can refactor the design by creating separate interfaces for 2D and 3D shapes.

class TwoDShape(ABC):
    @abstractmethod
    def area(self):
        pass

class ThreeDShape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def volume(self):
        pass

class Circle(TwoDShape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
class Cube(ThreeDShape):
    def __init__(self, side: float):
        self.side = side

    def area(self):
        return 6 * self.side * self.side

    def volume(self):
        return self.side * self.side * self.side

