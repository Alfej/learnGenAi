# Liskove Substitution Principle (LSP)
# This principle states that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.
# from abc import ABC, abstractmethod
# class Account(ABC):
#     @abstractmethod
#     def deposit(self, amount: int):
#         pass
    
#     @abstractmethod
#     def withdraw(self, amount: int):
#         pass

# class SavingsAccount(Account):
#     def __init__(self, balance: int = 0):
#         self.balance = balance

#     def deposit(self, amount: int):
#         if amount <= 0:
#             raise ValueError("Deposit amount must be positive")
#         print(f"Depositing {amount} to SavingsAccount")
#         self.balance += amount

#     def withdraw(self, amount: int):
#         if amount > self.balance:
#             raise ValueError("Insufficient funds")
#         print(f"Withdrawing {amount} from SavingsAccount")
#         self.balance -= amount
    
# class CurrentAccount(Account):
#     def __init__(self, balance: int = 0, overdraft_limit: int = 500):
#         self.balance = balance
#         self.overdraft_limit = overdraft_limit

#     def deposit(self, amount: int):
#         if amount <= 0:
#             raise ValueError("Deposit amount must be positive")
#         print(f"Depositing {amount} to CurrentAccount")
#         self.balance += amount

#     def withdraw(self, amount: int):
#         if amount > self.balance + self.overdraft_limit:
#             raise ValueError("Insufficient funds including overdraft limit")
#         print(f"Withdrawing {amount} from CurrentAccount")
#         self.balance -= amount
# # problem statement suppose we got another account as FixedDepositAccount which does not allow withdrawal before maturity. if we inherit it from Account class, it will violate LSP as it cannot perform withdraw operation.
# class FixedDepositAccount(Account):
#     def __init__(self, balance: int = 0, maturity_period: int = 12):
#         self.balance = balance
#         self.maturity_period = maturity_period
#         self.is_matured = False

#     def deposit(self, amount: int):
#         if amount <= 0:
#             raise ValueError("Deposit amount must be positive")
#         print(f"Depositing {amount} to FixedDepositAccount")
#         self.balance += amount

#     def withdraw(self, amount: int):
#         if not self.is_matured:
#             raise ValueError("Cannot withdraw before maturity")
#         if amount > self.balance:
#             raise ValueError("Insufficient funds")
#         print(f"Withdrawing {amount} from FixedDepositAccount")
#         self.balance -= amount 
# class user:
#     def __init__(self, accounts: list[Account]):
#         self.accounts = accounts

#     def perform_transactions(self):
#         for account in self.accounts:
#             account.deposit(1000)
#             account.withdraw(500)
#             print(f"Remaining balance: {account.balance}")

# if __name__ == "__main__":
#     savings = SavingsAccount(2000)
#     current = CurrentAccount(1000)
#     fixed_deposit = FixedDepositAccount(5000) # This will violate LSP if we try to withdraw

#     user1 = user([savings, current, fixed_deposit])
#     user1.perform_transactions()

# To adhere to LSP, we can refactor the design by creating a separate interface for withdrawable and non-withdrawable accounts.
from abc import ABC, abstractmethod
class NonWithdrawableAccount(ABC):
    @abstractmethod
    def deposit(self, amount: int):
        pass

class WithdrawableAccount(ABC):
    @abstractmethod
    def deposit(self, amount: int):
        pass
    
    @abstractmethod
    def withdraw(self, amount: int):
        pass

class SavingsAccount(WithdrawableAccount):
    def __init__(self, balance: int = 0):
        self.balance = balance

    def deposit(self, amount: int):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        print(f"Depositing {amount} to SavingsAccount")
        self.balance += amount

    def withdraw(self, amount: int):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        print(f"Withdrawing {amount} from SavingsAccount")
        self.balance -= amount

class CurrentAccount(WithdrawableAccount):
    def __init__(self, balance: int = 0, overdraft_limit: int = 500):
        self.balance = balance
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount: int):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        print(f"Depositing {amount} to CurrentAccount")
        self.balance += amount

    def withdraw(self, amount: int):
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Insufficient funds including overdraft limit")
        print(f"Withdrawing {amount} from CurrentAccount")
        self.balance -= amount

class FixedDepositAccount(NonWithdrawableAccount):
    def __init__(self, balance: int = 0, maturity_period: int = 12):
        self.balance = balance
        self.maturity_period = maturity_period
        self.is_matured = False

    def deposit(self, amount: int):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        print(f"Depositing {amount} to FixedDepositAccount")
        self.balance += amount

    def withdraw(self, amount: int):
        if not self.is_matured:
            raise ValueError("Cannot withdraw before maturity")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        print(f"Withdrawing {amount} from FixedDepositAccount")
        self.balance -= amount

class user:
    def __init__(self, withdrawable_accounts: list[WithdrawableAccount], non_withdrawable_accounts: list[NonWithdrawableAccount] = []):
        self.accounts = withdrawable_accounts
        self.non_withdrawable_accounts = non_withdrawable_accounts

    def perform_transactions(self):
        for account in self.accounts:
            account.deposit(1000)
            account.withdraw(500)
            print(f"Remaining balance: {account.balance}")

        for account in self.non_withdrawable_accounts:
            account.deposit(1000)
            print(f"Remaining balance: {account.balance}")

if __name__ == "__main__":
    savings = SavingsAccount(2000)
    current = CurrentAccount(1000)
    fixed_deposit = FixedDepositAccount(5000) # This will violate LSP if we try to withdraw

    user1 = user([savings, current], [fixed_deposit])
    user1.perform_transactions()


# guidelines to take care to achieve LSP:
# 1. Signature Rule: The method signatures in the subclass should match those in the superclass. This includes the method name, return type, and parameters.
#       Broad=> Parent class / Ancestor class
#       Narrow=> Child class / Descendant class
#       1. Method Argument Rule: Broad method signature should be followed in Narrow method signature
#       e.g., if parent class method is def add(int a, int b) -> int: then child class method should also be def add(int a, int b) -> int:
#       If parameter except a class type object, then we can use same or broader type in child class method
# ex.
# class Parent:
#     def add(self, a: int, b: int) -> int:
#         return a + b
# class Child(Parent):
#     def add(self, a: float, b: float) -> float: # Broader type
#         return int(a + b)

#       2. Return Type Rule(Covariance): Child inhariting parent should return same or narrower type than parent method
# ex.
# class Parent:
#     def get_value(self) -> object:
#         return "Parent Value"
# class Child(Parent):
#     def get_value(self) -> str: # Narrower type
#         return "Child Value"

#      3. Exception Rule: Child class method should not throw broader exceptions than parent class method
# Exception hierarchy: BaseException > Exception > StandardError > ValueError
# ex.
# class Parent:
#     def do_something(self) -> None:
#         pass
# class Child(Parent):
#     def do_something(self) -> None:
#         raise ValueError("Child error")

# 2. Property Rule:
#    1. Class Invariant Rule: The invariants of the parent class must be preserved in the child class.
        # An invariant is a condition that should always hold true for an object of a class.

        # ex. If a parent class has an invariant that a balance should never be negative, the child class must also ensure that the balance remains non-negative.
#    2. History Constraint Rule: The history of the parent class must be preserved in the child class.
        # The history of an object includes all the states it has gone through during its lifetime.
#       ex. If a parent class has a method that modifies the state of an object, the child class must ensure that the state transitions remain valid according to the parent's history.

# 3. Method Rule: 
#     1. pre-condition Rule: The pre-conditions of the parent class method must be preserved or weakened in the child class method.
        # A pre-condition is a condition that must be true before a method is executed.
        # ex. If a parent class method requires a positive integer as input, the child class method can accept any integer (positive, negative, or zero).

#     2. post-condition Rule: The post-conditions of the parent class method must be preserved or strengthened in the child class method.
        # A post-condition is a condition that must be true after a method has been executed.
        # ex. If a parent class method guarantees that the output will be a non-negative integer, the child class method can guarantee that the output will be a positive integer.