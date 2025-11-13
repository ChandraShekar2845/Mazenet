class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f"BankAccount(account_holder={self.account_holder}, balance={self.balance})"

acc = BankAccount("John Doe", 1000)
acc.deposit(500)
print(f"Balance after deposit: {acc.get_balance()}")     
acc.withdraw(200)
print(f"Balance after withdrawal: {acc.get_balance()}")