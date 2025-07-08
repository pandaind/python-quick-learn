"""
# Functional Programming Concepts

# Functional programming is a programming paradigm where you use functions to solve problems.

# Higher-Order Functions
def apply_function(func, value):
    return func(value)

def square(x):
    return x ** 2

print(apply_function(square, 5))  # Output: 25

# Map, Filter, and Reduce
numbers = [1, 2, 3, 4, 5]

# Map
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

# Filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Reduce
from functools import reduce
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)

# Interview Tip:
# Be prepared to explain the difference between imperative and functional programming.

# Common Interview Question:
# How can you use the `map` function to apply a function to all elements in a list?
# Use `map(function, iterable)` to apply the function to each element.
"""