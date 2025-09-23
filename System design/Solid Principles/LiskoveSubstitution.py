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