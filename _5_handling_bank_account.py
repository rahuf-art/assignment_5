class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.interestRate * self.balance) / 100

title = input("Enter the account title: ")
balance = float(input("Enter the initial balance: "))
interestRate = float(input("Enter the interest rate for savings account: "))

savings_account = SavingsAccount(title, balance, interestRate)

# Deposit and Withdrawal
deposit_amount = float(input("Enter the deposit amount: "))
savings_account.deposit(deposit_amount)

withdrawal_amount = float(input("Enter the withdrawal amount: "))
savings_account.withdrawal(withdrawal_amount)

# Get balance and calculate interest amount
print(f"Account Balance: {savings_account.getBalance()}")
interest_amount = savings_account.interestAmount()
print(f"Interest Amount: {interest_amount}")
