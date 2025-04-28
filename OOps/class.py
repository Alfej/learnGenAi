class Atm:
    def __init__(self):
        self.__pin = ""
        self.__balance = 0
        self.__menu()

    def __menu(self):
        user_input = input("""
                    Hello, How would you like to preoceed?
                           1.Enter 1 to create pin
                           2.Enter 2 to deposit
                           3.Enter 3 to withdraw
                           4.Enter 4 to check balance
                           5.Enter 5 to exit
                    """)
        if user_input=='1':
            print("Selected Create Pin.")
            self.create_pin()
        elif user_input=='2':
            print("Selected deposit.")
            self.deposit()
        elif user_input=='3':
            print("Selected withdraw.")
            self.withdraw()
        elif user_input=='4':
            print("Selected check balance.")
            self.check_balance()
        elif user_input=='5':
            print("Selected exit.")

    def create_pin(self):
        self.__pin = input("Enter PIN: ")
        print("PIN set successfully.")
    
    def deposit(self):
        temp = input("Enter your PIN: ")
        if temp==self.__pin:
            amount = int(input("Enter Amount: "))
            self.__balance = self.__balance+amount 
            print("Deposite successful.")
        else:
            print("Entered Wrong pin.")
    
    def withdraw(self):
        temp = input("Enter your PIN: ")
        if temp==self.__pin:
            amount = int(input("Enter Amount: "))
            if amount>self.__balance:
                print("Insufficinet balance.")
            else:
                self.__balance = self.__balance+amount 
                print("withdrawal successful.")
        else:
            print("Entered Wrong pin.")
    def check_balance(self):
        temp = input("Enter your PIN: ")
        if temp==self.__pin:
            print(f"Your available balance is .{self.balance}")
        else:
            print("Entered Wrong pin.")
if __name__=="__main__":
    sbi = Atm()
    print(sbi.__balance)