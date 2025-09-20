"""
Bank Account Class
    Create a `BankAccount` class with attributes `owner` and `balance`.
    Implement methods `deposit(amount)` and `withdraw(amount)`. 
    The `withdraw` method should not allow withdrawals that exceed the balance.
    Add a `__str__` method to print a user-friendly summary.
"""

class BankAccount:
    """
    `BankAccount` class with attributes `owner` and `balance`
    """
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.owner} - Balance: {self.balance}"

    def deposit(self, amount):
        """
        Deposit `amount`
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraw `amount` only if enough balace available.
        """
        self.balance -= amount if self.balance >= amount else 0

cliente = BankAccount("José", 1000)
print(cliente)
cliente.deposit(200)
print(cliente)
cliente.withdraw(700)
print(cliente)
cliente.withdraw(1000)
print(cliente)
