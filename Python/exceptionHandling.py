# There are 2 scenarios where Program can crash:
#  1. there is a syntax error in the code -> Occurs at compile time
#  2. there is an exception in the code -> Occurs at runtime

#  Type of Exceptions:
#  IndexError : Raised when an index is out of range
#  KeyError : Raised when a dictionary key is not found
#  ValueError : Raised when a function receives an argument of correct type but inappropriate value
#  ZeroDivisionError : Raised when division by zero is attempted
#  FileNotFoundError : Raised when a file is not found
#  ImportError : Raised when an import statement fails
#  ModuleNotFoundError : Raised when a module is not found
#  NameError : Raised when a variable is not found
#  TypeError : Raised when an operation is performed on an inappropriate type
#  AttributeError : Raised when an attribute is not found
#  RuntimeError : Raised when an error occurs that doesn't fall under any other category


import json


try:
    with open("Python/data.json", "r") as f:
        data = json.load(f)
        print(data)
except FileNotFoundError:
    print("File not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e.message}")

### 
# Multiple Exceptions can be handled in a single except block by using a tuple of exception types. For example:
# try:
#     with open("Python/data.json", "r") as f:
#         data = json.load(f)
#         print(data)
# except FileNotFoundError as e:
#     print(f"File not found: {e}")
# except json.JSONDecodeError as e:
#     print(f"JSON decode error: {e}")
# except Exception as e:
#     print(f"An error occurred: {e}")

# try, Except, Else

try:
    f = open("Python/data.json", "r")

except FileNotFoundError:
    print("File not found. Please check the file path.")

except Exception as e:
    print(f"An error occurred: {e}")

# Whn you want to execute some code only if no exception was raised in the try block, you can use the else block. The else block will be executed only if the try block did not raise any exceptions.
else:
    data = json.load(f)
    print(data)
    f.close()

# try, Except, Finally

try:
    f = open("Python/data.json", "r")

except FileNotFoundError:
    print("File not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    data = json.load(f)
    print(data)
finally:
    f.close()  # This will be executed regardless of whether an exception was raised or not


#  Raise an Exception

# We can raise an exception in Python using the `raise` statement. This can be useful when we want to indicate that an error has occurred in our code. For example, we can raise a `ValueError` if a function receives an argument of the correct type but an inappropriate value.
class InssufficientFundsError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class negativeAmountError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount < 0:
            raise negativeAmountError("Amount must be positive")
        if amount > self.balance:
            raise InssufficientFundsError("Insufficient funds")
        self.balance -= amount
        return self.balance

obj = BankAccount(1000)
try:
    obj.withdraw(-100)
except InssufficientFundsError as e:
    print(f"Insufficient funds: {e}")
except negativeAmountError as e:
    print(f"Invalid amount: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"Withdrawal successful. New balance: {obj.balance}") 