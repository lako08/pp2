class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b != 0:
            return a / b
        return "Cannot divide by zero"

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
    
    def get_balance(self):
        return self.balance

calc = Calculator()
print(calc.add(5, 3))
print(calc.subtract(10, 4))
print(calc.multiply(3, 7))
print(calc.divide(15, 3))

account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
print(account.get_balance())