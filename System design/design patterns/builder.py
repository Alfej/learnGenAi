# Builder is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.
# You can go further and extract a series of calls to the builder steps you use to construct a product into a separate class called director. The director class defines the order in which to execute the building steps, while the builder provides the implementation for those steps.
# Applicability 
# Use the Builder pattern when: 
# Use the Builder pattern to get rid of a “telescoping constructor”.
# A telescoping constructor is a constructor with many parameters, some of which are optional. The Builder pattern lets you construct an object step by step, allowing you to set only the parameters you need.
# Use the Builder pattern when you want your code to be able to create different representations of some product (for example, stone and wooden houses).

from __future__ import annotations
from abc import ABC, abstractmethod

class builder(ABC):
    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def set_seats(self) -> None:
        pass

    @abstractmethod
    def set_engine(self) -> None:
        pass
    
    @abstractmethod
    def set_tripCalc(self) -> None:
        pass
    
    @abstractmethod
    def set_gps(self) -> None:
        pass
    
class carBuilder(builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = car()

    def set_seats(self) -> None:
        self._product.seats = 4

    def set_engine(self) -> None:
        self._product.engine = "V8"

    def set_tripCalc(self) -> None:
        self._product.tripCalc = True

    def set_gps(self) -> None:
        self._product.gps = True

class manualBuilder(builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = manual()

    def set_seats(self) -> None:
        self._product.seats = "Car with 4 seats"
    def set_engine(self) -> None:
        self._product.engine = "V8 engine"

    def set_tripCalc(self) -> None:
        self._product.tripCalc = "Trip calculator exist"

    def set_gps(self) -> None:
        self._product.gps = "GPS exist"

class car():
    def __init__(self) -> None:
        self.seats = None
        self.engine = None
        self.tripCalc = None
        self.gps = None

    def __str__(self) -> str:
        return f"Car with {self.seats} seats, {self.engine} engine, {self.tripCalc}, {self.gps}"
    
class manual():
    def __init__(self) -> None:
        self.seats = None
        self.engine = None
        self.tripCalc = None
        self.gps = None

    def __str__(self) -> str:
        return f"Manual with {self.seats} seats, {self.engine} engine, {self.tripCalc}, {self.gps}"
    
class director():
    def __init__(self, builder: builder) -> None:
        self._builder = builder

    def build_ordinary_car(self) -> None:
        self._builder.set_seats()
        self._builder.set_engine()

    def build_exclusive(self) -> None:
        self._builder.set_seats()
        self._builder.set_engine()
        self._builder.set_tripCalc()
        self._builder.set_gps()
        
# Client code
if __name__ == "__main__":
    car_builder = carBuilder()
    manual_builder = manualBuilder()

    director1 = director(car_builder)
    director1.build_ordinary_car()
    print(car_builder._product)

    director1 = director(manual_builder)
    director1.build_ordinary_car()
    print(manual_builder._product)
    
    director2 = director(car_builder)
    director2.build_exclusive()
    print(car_builder._product)

    director2 = director(manual_builder)
    director2.build_exclusive()
    print(manual_builder._product)