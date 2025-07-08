"""
# Basics of Concurrency

# Concurrency allows you to run multiple tasks simultaneously.

# Using the `threading` Library
import threading

def print_numbers():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()

# Using the `asyncio` Library
import asyncio

async def async_print_numbers():
    for i in range(5):
        print(i)
        await asyncio.sleep(1)

asyncio.run(async_print_numbers())

# Interview Tip:
# Be ready to explain the difference between threading and asyncio.

# Common Interview Question:
# How can you create a simple thread in Python?
# Use the `threading.Thread` class and call the `start()` method.
"""