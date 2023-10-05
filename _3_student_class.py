class Student:
    def __init__(self):
        #uninitialized in the constructor
        pass

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getRollNumber(self):
        return self.__rollNumber

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber


student = Student()

# Initialize the name and roll number using setter methods
name = input("Enter the student's name: ")
student.setName(name)

rollNumber = input("Enter the student's roll number: ")
student.setRollNumber(rollNumber)

# Retrieve and print the values using getter methods
print(f"Student Name: {student.getName()}")
print(f"Roll Number: {student.getRollNumber()}")
