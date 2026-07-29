#  Decorators are a way to modify or enhance functions or methods in Python. They allow you to wrap another function in order to extend its behavior without permanently modifying it.

#  A decorator is a function that takes another function as an argument and returns a new function that adds some kind of functionality to the original function. Decorators are often used for logging, access control, memoization, and other cross-cutting concerns.

#  2 types of decorators in Python:
#  1. user-defined decorators: These are custom decorators created by the user to add specific functionality to functions or methods.
#  2. built-in decorators: These are decorators provided by Python's standard library, such as @staticmethod, @classmethod, and @property.

def my_decorator(func):
    def wrapper():
        print("*********************************")
        result = func()
        print("*********************************")
        return result
    return wrapper

def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
    return wrapper

@my_decorator
@timer
def say_hello():
    print("Hello!")


# # Applying the decorator to the function
# decorated_say_hello = my_decorator(say_hello)
# decorated_say_hello()

say_hello()  # This will print the output with the decorator applied


#  Same as Decorator design pattern in OOP, where we can add new functionality to an existing object without altering its structure. In Python, decorators are a powerful tool that allows us to achieve this in a clean and elegant way.