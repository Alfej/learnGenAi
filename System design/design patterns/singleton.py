# Creational design pattern
# insures class has one instance and provides a global point of access to it
# Example: Database connection, Logger, Configuration manager

# Use the Singleton pattern when a class in your program should have just a single instance available to all clients; for example, a single database object shared by different parts of the program.

# what is meta class?
# A metaclass is a class of a class that defines how a class behaves. A class is an instance of a metaclass. In Python, the default metaclass is type. You can create your own metaclass by inheriting from type.
# A metaclass can be used to customize class creation, modify class attributes, and enforce constraints on class definitions
# A metaclass is defined by inheriting from the type class. It can override methods like __new__ and __init__ to customize class creation and initialization.

class SingletonMeta(type):
    
    _instances={}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super.__call__(cls, *args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
    
class Singleton(metaclass=SingletonMeta):
    pass


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    
    print(s1 is s2)  # True, both variables point to the same instance
    print(id(s1), id(s2))  # Both IDs will be the same, confirming they are the same instance