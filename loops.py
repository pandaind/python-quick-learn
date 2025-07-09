"""
# Loops

# Loops are used to execute a block of code repeatedly as long as a condition is true (`while` loop)
# or for each item in a sequence (`for` loop).

print("--- 1. `for` Loops ---")
# `for` loops are used for iterating over a sequence (like a list, tuple, dictionary, set, or string)
# or other iterable objects.

print("Iterating over a range:")
for i in range(5): # range(5) generates numbers from 0 up to (but not including) 5
    print(i)       # Output: 0, 1, 2, 3, 4

print("\\nIterating over a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("\\nIterating over a string:")
for char in "Python":
    print(char)

print("\\nIterating over a tuple:")
colors = ("red", "green", "blue")
for color in colors:
    print(color)

print("\\nIterating over dictionary keys (default behavior):")
my_dict = {"a": 1, "b": 2, "c": 3}
for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}")

print("\\nIterating over dictionary values:")
for value in my_dict.values():
    print(f"Value: {value}")

print("\\nIterating over dictionary items (key-value pairs):")
for key, value in my_dict.items():
    print(f"Key: {key} => Value: {value}")

print("\\n" + "-"*60 + "\\n")
print("--- 2. `while` Loops ---")
# `while` loops repeat as long as a certain boolean condition is met.

count = 0
print("While loop example:")
while count < 5:
    print(f"Count is {count}")
    count += 1 # Important: Increment counter to avoid an infinite loop
print("While loop finished.")

# Example: Simple number guessing game
# secret_number = 7
# guess = 0
# print("\\nGuessing game (type a number, 7 to win):")
# while guess != secret_number:
#     try:
#         guess = int(input("Guess the number: "))
#         if guess != secret_number:
#             print("Try again!")
#     except ValueError:
#         print("Please enter a valid number.")
# print("Congratulations, you guessed it!")

print("\\n" + "-"*60 + "\\n")
print("--- 3. Loop Control Statements ---")
# `break`: Terminates the current loop prematurely.
# `continue`: Skips the rest of the code inside the current iteration and proceeds to the next iteration.
# `pass`: Does nothing. It can be used as a placeholder when a statement is required syntactically but no code needs to be executed.

print("`break` statement example:")
for i in range(10):
    if i == 5:
        print("Breaking loop at i=5")
        break # Exit the loop when i is 5
    print(i)

print("\\n`continue` statement example:")
for i in range(5):
    if i == 2:
        print("Skipping i=2 with continue")
        continue # Skip the rest of this iteration when i is 2
    print(i)

print("\\n`pass` statement example:")
for i in range(3):
    if i == 1:
        pass # Placeholder, e.g., if logic for i=1 is not yet implemented
        print("Pass statement executed (did nothing on its own).")
    print(i)

def my_empty_function(): # pass is often used for stubs
    pass

print("\\n" + "-"*60 + "\\n")
print("--- 4. `else` Clause in Loops ---")
# Python loops (`for` and `while`) can have an optional `else` clause.
# The `else` block executes if the loop completes normally (i.e., not terminated by a `break` statement).

print("`for...else` example (loop completes normally):")
for i in range(3):
    print(f"For loop iteration {i}")
else:
    print("For loop completed without a break.") # This will execute

print("\\n`for...else` example (loop broken):")
for i in range(5):
    print(f"For loop iteration {i}")
    if i == 2:
        print("Breaking the for loop.")
        break
else:
    print("For loop completed without a break. (This will NOT execute)")

print("\\n`while...else` example (loop completes normally):")
c = 0
while c < 3:
    print(f"While loop iteration {c}")
    c += 1
else:
    print("While loop completed without a break.") # This will execute

print("\\n`while...else` example (loop broken):")
c = 0
while c < 5:
    print(f"While loop iteration {c}")
    if c == 2:
        print("Breaking the while loop.")
        break
    c += 1
else:
    print("While loop completed without a break. (This will NOT execute)")

# Use case: Searching for an item. The `else` block can run if the item wasn't found.
items = ["apple", "banana", "orange"]
search_item = "grape"
print(f"\\nSearching for '{search_item}' in {items}:")
for item in items:
    if item == search_item:
        print(f"Found '{search_item}'!")
        break
else: # Executes if the loop finished without finding the item (no break)
    print(f"'{search_item}' not found in the list.")


print("\\n" + "-"*60 + "\\n")
print("--- 5. `enumerate()` Function ---")
# `enumerate()` is used when you need both the index and the value of items in an iterable.
# It returns an enumerate object, which yields pairs of (index, value).

my_fruits = ["apricot", "blueberry", "cantaloupe"]
print("Using `enumerate()`:")
for index, fruit_name in enumerate(my_fruits):
    print(f"Index: {index}, Fruit: {fruit_name}")

# You can also specify a starting index for enumerate:
print("\\nUsing `enumerate()` with a start index of 1:")
for index, fruit_name in enumerate(my_fruits, start=1):
    print(f"Item No.: {index}, Fruit: {fruit_name}")

print("\\n" + "-"*60 + "\\n")
print("--- 6. `zip()` Function ---")
# `zip()` is used to combine multiple iterables element-wise into an iterator of tuples.
# It stops when the shortest iterable is exhausted.

names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]
cities = ["New York", "London", "Paris", "Tokyo"] # Tokyo will be ignored as it's longer

print("Using `zip()` to combine names and ages:")
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

print("\\nUsing `zip()` to combine names, ages, and cities:")
for name, age, city in zip(names, ages, cities): # Stops after Charlie/35/Paris
    print(f"{name} (age {age}) lives in {city}.")

# If you want to zip to the length of the longest iterable, use `itertools.zip_longest`.
from itertools import zip_longest
print("\\nUsing `itertools.zip_longest()`:")
for name, age, city in zip_longest(names, ages, cities, fillvalue="N/A"):
    print(f"Name: {name}, Age: {age}, City: {city}")


# Interview Tip:
# - Be ready to explain the difference between `for` and `while` loops.
# - Understand loop control statements: `break`, `continue`, and `pass`.
# - The `else` clause in loops is a unique Python feature; know when it executes.
# - `enumerate()` for getting index and value, and `zip()` for parallel iteration are very handy.

# Common Interview Question:
# Q: How can you iterate over a list using a loop in Python?
# A: You can use a `for` loop directly: `for item in my_list: print(item)`.
#    If you need the index as well, use `enumerate()`: `for index, item in enumerate(my_list): print(index, item)`.
#
# Q: When does the `else` block of a loop execute?
# A: The `else` block of a `for` or `while` loop executes if and only if the loop terminates
#    normally (i.e., it runs through all its iterations for a `for` loop, or its condition
#    becomes false for a `while` loop), and not when the loop is exited by a `break` statement.
"""