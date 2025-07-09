"""
# Conditional Statements

# Conditional Statements

# Conditional statements are used to execute different blocks of code based on whether
# a certain condition is true or false.

print("--- 1. `if`, `elif`, and `else` Statements ---")
# The most common conditional structure.
temperature = 20

print(f"Current temperature: {temperature}°C")
if temperature > 30:
    print("It's a very hot day!")
    print("Stay hydrated.")
elif temperature > 25: # 'elif' is short for 'else if'
    print("It's a hot day.")
elif temperature > 15:
    print("It's a pleasant warm day.")
elif temperature >= 0:
    print("It's a bit chilly.")
else: # Optional, executes if none of the preceding conditions were true.
    print("It's a cold day! Bundle up.")

# Only one block (if, elif, or else) will be executed.

print("\\n" + "-"*60 + "\\n")
print("--- 2. Truth Value Testing ---")
# In Python, various values are implicitly treated as `False` in a boolean context.
# Any value that is not considered "false" is considered "true".

# Values considered False (Falsy values):
# - `None`
# - `False` (the boolean value)
# - Zero of any numeric type: `0`, `0.0`, `0j`
# - Empty sequences: `''` (empty string), `[]` (empty list), `()` (empty tuple)
# - Empty mappings: `{}` (empty dictionary)
# - Empty sets: `set()`
# - Objects of user-defined classes, if the class defines a `__bool__()` method that returns `False`
#   or a `__len__()` method that returns `0`.

print("Examples of Falsy values:")
falsy_values = [None, False, 0, 0.0, "", [], (), {}, set()]
for val in falsy_values:
    if val: # Condition will be False
        print(f"{repr(val)} is Truthy (This should not print)")
    else: # This block will execute
        print(f"{repr(val)} is Falsy")

print("\\nExamples of Truthy values:")
truthy_values = [True, 1, -1, 0.1, "hello", [1, 2], {"a": 1}, {1}]
for val in truthy_values:
    if val: # Condition will be True
        print(f"{repr(val)} is Truthy")
    else:
        print(f"{repr(val)} is Falsy (This should not print)")

# This is useful for concise checks:
my_list = []
if my_list: # This is False because my_list is empty
    print("List has items.")
else:
    print("List is empty.")

name = "Alice"
if name: # This is True because non-empty strings are truthy
    print(f"Name is: {name}")

print("\\n" + "-"*60 + "\\n")
print("--- 3. Ternary Operator (Conditional Expressions) ---")
# A concise way to write a simple if-else statement in a single line.
# Syntax: `value_if_true if condition else value_if_false`

age = 22
status = "Adult" if age >= 18 else "Minor"
print(f"Age: {age}, Status: {status}") # Output: Age: 22, Status: Adult

age = 15
status = "Adult" if age >= 18 else "Minor"
print(f"Age: {age}, Status: {status}") # Output: Age: 15, Status: Minor

# Can be used in assignments, print statements, etc.
max_val = 100
min_val = 10
b = 50
result = "Within range" if min_val <= b <= max_val else "Out of range"
print(f"b={b} is '{result}' for range [{min_val}, {max_val}]")

# While concise, they can become hard to read if overused or too complex.
# For more complex logic, a full if-else statement is usually better.

# Example: Assigning a default value
user_input = "" # or None
# user_input = "Jules"
username = user_input if user_input else "Guest" # If user_input is falsy (empty string, None), use "Guest"
print(f"Username: {username}")


print("\\n" + "-"*60 + "\\n")
# Interview Tip:
# - Be prepared to explain the difference between `if`, `elif`, and `else` statements and how only one block executes.
# - Understand Python's truth value testing (which values are considered False).
# - Know the syntax and use cases for the ternary operator (conditional expression) for simple conditions.

# Common Interview Question:
# Q: How does Python handle indentation in conditional statements?
# A: Python uses indentation (typically 4 spaces per level) to define the scope or block of code
#    that belongs to a conditional statement (if, elif, else). Consistent indentation is crucial
#    as it's part of Python's syntax, not just for style. Incorrect indentation leads to
#    IndentationError or logical errors.
#
# Q: What are "falsy" values in Python? Give examples.
# A: Falsy values are values that Python treats as `False` in a boolean context. Examples include
#    `None`, `False`, `0` (integer), `0.0` (float), empty string `""`, empty list `[]`,
#    empty tuple `()`, empty dictionary `{}`, and empty set `set()`.
"""