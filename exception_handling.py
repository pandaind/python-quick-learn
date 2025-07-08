"""
# Exception Handling

# Exception handling allows you to handle errors gracefully without crashing the program.

# Try/Except Block
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Try/Except/Finally Block
try:
    file = open("example.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    print("This block always executes.")

# Custom Exceptions
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error!")
except CustomError as e:
    print(e)

# Interview Tip:
# Be prepared to explain the difference between exceptions and errors in Python.

# Common Interview Question:
# How can you create and raise a custom exception in Python?
# Define a class that inherits from the `Exception` class and use the `raise` keyword to raise it.
"""