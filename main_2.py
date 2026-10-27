# main.py
# Aidan's Goy Bank - a simple banking program.

import math

from bank_account import BankAccount


def get_amount(prompt):
    """Ask for a dollar amount.

    Returns the amount as a float rounded to cents, or None if the input was not a number.
    """
    amount_text = input(prompt).strip().replace("$", "").replace(",", "")
    try:
        amount = float(amount_text)
    except ValueError:
        return None

    # Reject values like "nan" or "inf" that Python accepts as floats.
    if not math.isfinite(amount):
        return None

    # Round to cents so the amount shown always matches the amount used.
    return round(amount, 2)


def make_deposit(account):
    """Ask the customer how much to deposit and add it to the account."""
    amount = get_amount("How much would you like to deposit? ")

    if amount is None:
        print("Invalid amount. Please enter a number.")
    elif account.deposit(amount):
        print(f"Deposited ${amount:,.2f}. New balance: ${account.get_balance():,.2f}")
    else:
        print("Deposit must be greater than $0.00.")


def make_withdrawal(account):
    """Ask the customer how much to withdraw and remove it from the account."""
    amount = get_amount("How much would you like to withdraw? ")

    if amount is None:
        print("Invalid amount. Please enter a number.")
    elif amount <= 0:
        print("Withdrawal must be greater than $0.00.")
    elif amount > account.get_balance():
        print(f"Insufficient funds. Your balance is ${account.get_balance():,.2f}.")
    else:
        account.withdraw(amount)
        print(f"Withdrew ${amount:,.2f}. New balance: ${account.get_balance():,.2f}")


def view_account_info(account):
    """Display the customer's name, account number, and balance."""
    account.display_info()


def display_menu():
    """Print the menu of options."""
    print("\nPlease choose an option:")
    print("1. Make a deposit")
    print("2. Make a withdrawal")
    print("3. View account information")
    print("4. Quit")


def main():
    """Create the customer's account and run the menu until they quit."""
    print("Welcome to the Bank of Spencer!")

    # Keep asking until the customer enters a name.
    customer_name = ""
    while customer_name == "":
        customer_name = input("Please enter your name: ").strip()

    account = BankAccount(customer_name)

    choice = ""
    while choice != "4":
        display_menu()
        choice = input().strip()

        if choice == "1":
            make_deposit(account)
        elif choice == "2":
            make_withdrawal(account)
        elif choice == "3":
            view_account_info(account)
        elif choice == "4":
            print("Thank you for your business!")
        else:
            print("Invalid choice. Please try again.")


main()
