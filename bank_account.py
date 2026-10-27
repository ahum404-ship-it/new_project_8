# bank_account.py
# Defines the BankAccount class used by the Bank of Spencer program.

import random


class BankAccount:
    """Represents a customer's simple bank account."""

    def __init__(self, customer_name):
        """Create a new account with a random account number and $0.00 balance."""
        self.customer_name = customer_name
        self.account_number = random.randint(10000, 99999)
        self.balance = 0.0

    def deposit(self, amount):
        """Add money to the account.

        Returns True if the deposit worked, or False if the amount
        was not greater than zero.
        """
        if amount <= 0:
            return False
        self.balance = round(self.balance + amount, 2)
        return True

    def withdraw(self, amount):
        """Remove money from the account.

        Returns True if the withdrawal worked, or False if the amount
        was not greater than zero or is more than the current balance.
        """
        if amount <= 0 or amount > self.balance:
            return False
        self.balance = round(self.balance - amount, 2)
        return True

    def get_balance(self):
        """Return the current balance."""
        return self.balance

    def display_info(self):
        """Print the customer's name, account number, and balance."""
        print(f"Name: {self.customer_name}")
        print(f"Account #: {self.account_number}")
        print(f"Balance: ${self.balance:,.2f}")
