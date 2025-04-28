from __future__ import annotations
# Factory method is a creational design pattern which solves the problem of creating product objects without specifying their concrete classes.
# The Factory Method defines a method, which should be used for creating objects instead of using a direct constructor call (new operator). Subclasses can override this method to change the class of objects that will be created.

# example:
#     The Factory Method pattern is widely used in Python code. It’s very useful when you need to provide a high level of flexibility for your code.

from abc import ABC, abstractmethod


class vehicle(ABC):
    @abstractmethod
    def Seating(self) -> str:
        pass
    
class car(vehicle):
    def Seating(self) -> str:
        return "4 seats"
    
class bus(vehicle):
    def Seating(self) -> str:
        return "40 seats"

class bike(vehicle):
    def Seating(self) -> str:
        return "2 seats"
    
class vehicleFactory:
    def get_vehicle(self,type) -> vehicle:
        if type == "car":
            return car()
        elif type == "bus":
            return bus()
        elif type == "bike":
            return bike()
        else:
            raise ValueError("Unknown vehicle type")
        
factory = vehicleFactory()
car = factory.get_vehicle("car")
bus = factory.get_vehicle("bus")
bike = factory.get_vehicle("bike")

print(f"Car: {car.Seating()}")
print(f"Bus: {bus.Seating()}")
print(f"Bike: {bike.Seating()}")