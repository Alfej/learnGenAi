# Creational design pattern
# insures class has one instance and provides a global point of access to it
# Example: Database connection, Logger, Configuration manager

# Use the Singleton pattern when a class in your program should have just a single instance available to all clients; for example, a single database object shared by different parts of the program.

# what is meta class?
# A metaclass is a class of a class that defines how a class behaves. A class is an instance of a metaclass. In Python, the default metaclass is type. You can create your own metaclass by inheriting from type.
# A metaclass can be used to customize class creation, modify class attributes, and enforce constraints on class definitions
# A metaclass is defined by inheriting from the type class. It can override methods like __new__ and __init__ to customize class creation and initialization.


# without threading implementation
# class SingletonMeta(type):
    
#     _instances={}
    
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             instance = super().__call__(*args, **kwargs)
#             cls._instances[cls] = instance
#         return cls._instances[cls]


from threading import Lock,Thread
class SingletonMeta(type):
    
    _instances={}
    _lock : Lock = Lock()
    
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            # Check if an instance already exists
            if cls not in cls._instances:
                # Create a new instance and store it in the dictionary
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]
    
    
class Singleton(metaclass=SingletonMeta):
    
    def __init__(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
    
    def get_id(self):
        return id(self)

def test(value):
    singleton = Singleton(value)
    print(f"Singleton value: {singleton.get_value()}")
    print(f"Singleton ID: {singleton.get_id()}")

if __name__ == "__main__":
    process1 = Thread(target=test, args=("First Object",))
    process2 = Thread(target=test, args=("Second Object",))
    
    process1.start()
    process2.start() 