class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num1 == 0:
            return "Division by zero is not allowed."
        return self.num2 / self.num1

# Input values for num1 and num2
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Create a Calculator object with the user-input values
calculator = Calculator(num1, num2)

# Perform calculations and print the results
print(f"Addition: {calculator.add()}")
print(f"Subtraction: {calculator.subtract()}")
print(f"Multiplication: {calculator.multiply()}")
print(f"Division: {calculator.divide()}")
