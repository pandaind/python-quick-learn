"""
# Comprehensions

# Comprehensions provide a concise way to create lists, dictionaries, and sets.

# List Comprehension
squares = [x ** 2 for x in range(10)]
print(squares)

# Dictionary Comprehension
squared_dict = {x: x ** 2 for x in range(10)}
print(squared_dict)

# Set Comprehension
unique_squares = {x ** 2 for x in range(10)}
print(unique_squares)

# Interview Tip:
# Be ready to explain the advantages of using comprehensions over traditional loops.

# Common Interview Question:
# How can you use list comprehension to filter even numbers from a list?
# [x for x in numbers if x % 2 == 0]
"""