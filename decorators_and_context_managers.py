"""
# Decorators and Context Managers

# Decorators are a way to modify the behavior of a function. Context managers are used to manage resources.

# Creating a Decorator
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Creating a Context Manager
class MyContextManager:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

with MyContextManager():
    print("Inside context")

# Interview Tip:
# Be ready to explain the use cases for decorators and context managers.

# Common Interview Question:
# How can you create a context manager using the `with` statement in Python?
# Implement the `__enter__` and `__exit__` methods in a class.
"""