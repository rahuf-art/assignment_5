class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        # Square the values of x, y, and z and return their sum
        return self.x ** 2 + self.y ** 2 + self.z ** 2

# Input values from the user
x = float(input("Enter the value for x: "))
y = float(input("Enter the value for y: "))
z = float(input("Enter the value for z: "))

# Create a Point object with the user-input values
point = Point(x, y, z)

# Calculate and print the sum of squared values
result = point.sqSum()
print(f"The sum of squared values is: {result}")
