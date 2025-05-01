# Abstract Factory is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.
# commitng change
from __future__ import annotations
from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def specifications(self) -> str:
        pass
    
class BMW(vehicle):
    def specifications(self) -> str:
        return "BMW: 4 wheels, 2 doors, 5 seats"

class Mercedes(vehicle):
    def specifications(self) -> str:
        return "Mercedes: 4 wheels, 4 doors, 5 seats"
    
class Maruti(vehicle):
    def specifications(self) -> str:
        return "Maruti: 4 wheels, 4 doors, 5 seats, least expensive"
    
class vehicleabstractFactory(ABC):
    @abstractmethod
    def get_vehicle(self) -> vehicle:
        pass

class BMWFactory(vehicleabstractFactory):
    def get_vehicle(self) -> vehicle:
        return BMW()
    
class MercedesFactory(vehicleabstractFactory):
    def get_vehicle(self) -> vehicle:
        return Mercedes()
    
class MarutiFactory(vehicleabstractFactory):
    def get_vehicle(self) -> vehicle:
        return Maruti()
    
class vehicleFactory():
    def get_vehicle(self, factory) -> vehicle:
        return factory.get_vehicle()
    
# Client code
if __name__ == "__main__":
    factory = vehicleFactory()
    
    bmw = factory.get_vehicle(BMWFactory())
    print(bmw.specifications())
    
    maruti = factory.get_vehicle(MarutiFactory())
    print(maruti.specifications())