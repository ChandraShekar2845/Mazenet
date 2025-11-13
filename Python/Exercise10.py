# OOP – Encapsulation and Methods
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance    

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance!")

    def check_balance(self):
        return self.__balance

acc = BankAccount()
acc.deposit(500)
acc.withdraw(200)
print("Balance:", acc.check_balance())
