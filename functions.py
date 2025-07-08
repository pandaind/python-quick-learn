"""
# Functions

# Functions are blocks of reusable code that perform a specific task.

# Defining a Function
def greet(name):
    return f"Hello, {name}!"

# Calling a Function
print(greet("Alice"))

# Recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# Lambda Functions
square = lambda x: x ** 2
print(square(4))  # Output: 16

# Interview Tip:
# Be prepared to explain the difference between regular functions and lambda functions.

# Common Interview Question:
# What is recursion, and can you provide an example?
# Recursion is a function calling itself to solve smaller instances of a problem.
"""