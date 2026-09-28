class Account:
    def __init__(self, name: str) -> None:
        self.name = name.lower()
        self.balance = 0

    def deposit(self, amount: float):
        if(amount < 0):
            raise ValueError("Deposit amount be negative")
        self.balance += amount

    def withdraw(self, amount):
        if(amount < self.balance and amount > 0):
            self.balance -= amount
        else:
            raise ValueError("Deposit amount be negative")

