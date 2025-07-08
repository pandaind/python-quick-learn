"""
# Unit Testing

# Unit testing is a way to test individual units of code to ensure they work as expected.

# Using the `unittest` Library
import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

if __name__ == "__main__":
    unittest.main()

# Using the `pytest` Library
# Save the following code in a file named `test_add.py`:
# def test_add():
#     assert add(2, 3) == 5
#     assert add(-1, 1) == 0

# Interview Tip:
# Be prepared to explain the difference between `unittest` and `pytest`.

# Common Interview Question:
# How can you write a simple unit test in Python?
# Use the `unittest` library to create a test case class and define test methods.
"""