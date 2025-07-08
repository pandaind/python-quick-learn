"""
# Data Structures and Algorithms

# Data structures are used to store and organize data. Algorithms are used to manipulate data.

# Stack
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack.pop())  # Output: 3

# Queue
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)
print(queue.popleft())  # Output: 1

# Sorting
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

# Searching
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

print(linear_search(numbers, 9))  # Output: 2

# Interview Tip:
# Be ready to explain the time complexity of basic algorithms.

# Common Interview Question:
# How can you implement a stack using a list in Python?
# Use `append()` to push and `pop()` to pop elements from the list.
"""