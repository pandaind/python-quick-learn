"""
# Variables and Data Types

# Variables are used to store data. Python is dynamically typed, meaning you don't need to declare the type of a variable.

# Example:
name = "Alice"  # String
age = 25        # Integer
height = 5.5    # Float
is_student = True  # Boolean
no_value = None   # NoneType

# You can check the type of a variable using the `type()` function.
print(f"Type of name: {type(name)}")      # Output: <class 'str'>
print(f"Type of age: {type(age)}")       # Output: <class 'int'>
print(f"Type of height: {type(height)}")    # Output: <class 'float'>
print(f"Type of is_student: {type(is_student)}")  # Output: <class 'bool'>
print(f"Type of no_value: {type(no_value)}")  # Output: <class 'NoneType'>

# Type Casting (Converting between types)
# Python allows you to convert data types explicitly.

# Example: Integer to String
age_str = str(age)
print(f"Age as string: {age_str}, type: {type(age_str)}")

# Example: String to Integer (requires string to be a valid integer representation)
num_str = "100"
num_int = int(num_str)
print(f"String as integer: {num_int}, type: {type(num_int)}")

# Example: String to Float
float_str = "123.45"
num_float = float(float_str)
print(f"String as float: {num_float}, type: {type(num_float)}")

# Example: Integer to Float
float_val = float(age)
print(f"Integer as float: {float_val}, type: {type(float_val)}")

# Example: Float to Integer (truncates decimal part)
int_val = int(height)
print(f"Float as integer: {int_val}, type: {type(int_val)}")

# Example: To Boolean
# Most values convert to True, except for empty sequences/collections, zero, and None.
print(f"Boolean of 0: {bool(0)}")          # Output: False
print(f"Boolean of []: {bool([])}")        # Output: False
print(f"Boolean of None: {bool(None)}")    # Output: False
print(f"Boolean of 5: {bool(5)}")          # Output: True
print(f"Boolean of 'Hi': {bool('Hi')}")    # Output: True


# Interview Tip:
# Be prepared to explain the difference between mutable and immutable data types in Python.
# Mutable: Lists, Dictionaries, Sets
# Immutable: Strings, Tuples, Integers, Floats

# Common Interview Question:
# What is the difference between `is` and `==` in Python?
# `is` checks for object identity, while `==` checks for value equality.
"""