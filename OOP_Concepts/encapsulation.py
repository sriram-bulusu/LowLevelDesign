# ENCAPSULATION

class BankAccount:
    """
    
        initializing accountNumber and balance as private attributes, 
        meaning they can only be accessed through the class and not publicly

        THIS IS WHAT ENCAPSULATION MEANS!

        the '__' in front of the attribute name denotes that it's private 
    
    """
    def __init__(self, accountNumber, balance):
        self.__account_number = accountNumber
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposit of {amount} successful!")
    
    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            print(f"Withdrawal of {amount} successful!")
        else:
            print("Insufficient funds!")
    
    def check_balance(self):
        print(f"Account balance is {self.__balance}")


myAccount = BankAccount(500049, 3000)

myAccount.deposit(5000)
myAccount.deposit(2000)

myAccount.check_balance()

myAccount.withdraw(4000)
myAccount.check_balance()
myAccount.withdraw(8000)
