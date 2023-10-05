class Account:
    def __init__(self, title, balance=0):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

# Input values for title, balance, and interest rate
title = input("Enter the account title: ")
balance = float(input("Enter the account balance: "))
interestRate = float(input("Enter the interest rate: "))

savings_account = SavingsAccount(title, balance, interestRate)

# Print the details of the savings account
print(f"Account Title: {savings_account.title}")
print(f"Account Balance: {savings_account.balance}")
print(f"Interest Rate: {savings_account.interestRate}%")
