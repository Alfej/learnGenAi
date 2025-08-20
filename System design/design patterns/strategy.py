# Strategy is a behavioral design pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable./

# Applicability:
#  Use the Strategy pattern when you want to use different variants of an algorithm within an object and be able to switch from one algorithm to another during runtime.
#  Use the Strategy when you have a lot of similar classes that only differ in the way they execute some behavior
# Use the pattern to isolate the business logic of a class from the implementation details of algorithms that may not be as important in the context of that logic.
# Use the pattern when your class has a massive conditional statement that switches between different variants of the same algorithm.

from __future__ import annotations
from abc import ABC, abstractmethod

class MapsUI():

    def __init__(self, strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy.name

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy
    
    def get_map(self):
        fromPlace = input("Enter the starting point: ")
        toPlace = input("Enter the destination: ")

        return self._strategy.get_map(fromPlace, toPlace)
    
class MapStrategyInterface(ABC):

    @abstractmethod
    def get_map(self, fromPlace: str, toPlace: str) -> str:
        pass

class CarMapStrategy(MapStrategyInterface):

    def get_map(self, fromPlace: str, toPlace: str) -> str:
        return f"Car route from {fromPlace} to {toPlace}"
    
class BikeMapStrategy(MapStrategyInterface):
    
    def get_map(self, fromPlace: str, toPlace: str) -> str:
        return f"Bike route from {fromPlace} to {toPlace}"

class WalkMapStrategy(MapStrategyInterface):

    def get_map(self, fromPlace: str, toPlace: str) -> str:
        return f"Walking route from {fromPlace} to {toPlace}"

if __name__ == "__main__":
    maps_ui = MapsUI(CarMapStrategy())
    print(maps_ui.get_map())

    maps_ui.strategy = BikeMapStrategy()
    print(maps_ui.get_map())

    maps_ui.strategy = WalkMapStrategy()
    print(maps_ui.get_map())
    