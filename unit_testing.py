"""
# Unit Testing

# Unit Testing

# Unit testing is a software testing method by which individual units of source code—sets of
# one or more computer program modules together with associated control data, usage procedures,
# and operating procedures—are tested to determine whether they are fit for use.
# Python has a built-in module `unittest` and popular third-party libraries like `pytest`.

import unittest
from unittest.mock import patch, MagicMock # For mocking
import math # For a function to test

# --- Simple functions to test ---
def add(a, b):
    """Adds two numbers."""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Inputs must be numbers.")
    return a + b

def divide(a, b):
    """Divides a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

class SimpleMathOperations:
    """A simple class to demonstrate testing methods."""
    def multiply(self, a, b):
        return a * b

    def is_positive(self, num):
        return num > 0

print("--- 1. `unittest` Library ---")
# `unittest` is Python's built-in testing framework (inspired by JUnit).
# Key concepts:
# - Test cases are created by subclassing `unittest.TestCase`.
# - Test methods within the class must start with `test_`.
# - Various `assert` methods are provided by `TestCase` to check conditions.
# - Tests can be run by calling `unittest.main()` usually from `if __name__ == '__main__':`.

class TestMathFunctions(unittest.TestCase):
    """Test suite for our math functions and class."""

    @classmethod
    def setUpClass(cls):
        """Called once before all tests in this class run."""
        print("\\nSetting up TestMathFunctions class resources...")
        cls.math_ops = SimpleMathOperations() # Create an instance for all tests in this class

    @classmethod
    def tearDownClass(cls):
        """Called once after all tests in this class have run."""
        print("\\nTearing down TestMathFunctions class resources...")
        del cls.math_ops

    def setUp(self):
        """Called before each test method is executed."""
        print(f"  Setting up for test: {self.id()}...")
        # Example: self.data = [1,2,3] # If each test needs fresh data

    def tearDown(self):
        """Called after each test method has executed (even if it failed)."""
        print(f"  Tearing down after test: {self.id()}...")
        # Example: Clean up resources created in setUp

    def test_add_integers(self):
        """Test add function with integers."""
        self.assertEqual(add(2, 3), 5, "2+3 should be 5")
        self.assertEqual(add(-1, 1), 0, "-1+1 should be 0")
        self.assertEqual(add(0, 0), 0, "0+0 should be 0")

    def test_add_floats(self):
        """Test add function with floats."""
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7, msg="0.1+0.2 should be close to 0.3")
        self.assertAlmostEqual(add(1.0, 2.5), 3.5, places=7)

    def test_add_type_error(self):
        """Test add function raises TypeError for non-numeric input."""
        # self.assertRaises(TypeError, add, "2", 3)
        # self.assertRaises(TypeError, add, 2, "3")
        with self.assertRaises(TypeError, msg="Adding string and int should raise TypeError"):
            add("2", 3)
        with self.assertRaisesRegex(TypeError, "Inputs must be numbers."):
            add(2, "three")

    def test_divide_normal(self):
        """Test normal division."""
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context_manager:
            divide(10, 0)
        self.assertEqual(str(context_manager.exception), "Cannot divide by zero.")

    def test_simple_math_ops_multiply(self):
        """Test multiply method of SimpleMathOperations class."""
        # Using the class instance created in setUpClass
        self.assertEqual(self.math_ops.multiply(3, 4), 12)
        self.assertEqual(self.math_ops.multiply(-2, 5), -10)

    def test_simple_math_ops_is_positive(self):
        """Test is_positive method."""
        self.assertTrue(self.math_ops.is_positive(5), "5 should be positive")
        self.assertFalse(self.math_ops.is_positive(-5), "-5 should not be positive")
        self.assertFalse(self.math_ops.is_positive(0), "0 should not be positive")

    def test_list_membership(self):
        """Test list membership assertions."""
        my_list = ['apple', 'banana', 'cherry']
        self.assertIn('banana', my_list, "'banana' should be in the list")
        self.assertNotIn('grape', my_list, "'grape' should not be in the list")

    @unittest.skip("Demonstrating skipping a test")
    def test_skipped_example(self):
        self.fail("This test should have been skipped!")

    @unittest.skipIf(sys.version_info < (3, 10), "Skipping test that requires Python 3.10+")
    def test_python_3_10_feature(self):
        # Code that uses a Python 3.10+ feature
        self.assertTrue(True, "This runs only on Py3.10+")
        print("    (Executed test_python_3_10_feature)")


# To run unittest tests from the command line:
# `python -m unittest unit_testing.py`
# `python -m unittest discover` (discovers tests in current dir and subdirs)
# `python unit_testing.py` (if `unittest.main()` is present)

# For the `if __name__ == '__main__':` block to work when running the file directly:
# unittest.main() needs to be here, or you need to create a TestLoader and TestRunner setup.
# The simple `unittest.main()` is usually sufficient for single files.

print("\\n" + "-"*60 + "\\n")
print("--- 2. `pytest` Library (Third-Party) ---")
# `pytest` is a popular third-party testing framework known for its simple syntax and powerful features.
# - No need to subclass anything; test functions are typically plain functions.
# - Test function names should start or end with `test_`. Test class names should start with `Test`.
# - Uses plain `assert` statements for checks (more Pythonic).
# - Rich plugin architecture, fixtures, parametrization, etc.

# To use pytest:
# 1. Install it: `pip install pytest`
# 2. Write test files (e.g., `test_example.py` or `example_test.py`).
# 3. Run from the terminal: `pytest` (it auto-discovers tests).

# Example test functions for pytest (would typically be in a separate file like `test_my_math.py`):

# Content for a hypothetical `test_my_math_pytest.py` file:
PYTEST_EXAMPLE_CODE = """
import pytest
from unit_testing import add, divide # Assuming this file is unit_testing.py

def test_add_pytest():
    assert add(2, 3) == 5
    assert add(-1, -1) == -2

def test_divide_pytest():
    assert divide(10, 2) == 5

def test_divide_by_zero_pytest():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(10, 0)

# Pytest Fixtures: Reusable setup/teardown code for tests.
@pytest.fixture
def sample_list():
    print("\\n  (pytest fixture 'sample_list' setup)")
    return [1, 2, 3, 4, 5]

def test_list_length_with_fixture(sample_list): # Fixture is passed as an argument
    assert len(sample_list) == 5

# Pytest Parametrization: Run the same test with multiple inputs.
@pytest.mark.parametrize("input_a, input_b, expected", [
    (1, 2, 3),      # Test case 1
    (0, 0, 0),      # Test case 2
    (-1, 1, 0),     # Test case 3
    (0.5, 0.5, 1.0) # Test case 4
])
def test_add_parametrized(input_a, input_b, expected):
    assert add(input_a, input_b) == expected
"""
print("Pytest example code (would be in a file like `test_my_math_pytest.py`):")
print("```python" + PYTEST_EXAMPLE_CODE + "```")
print("\\nTo run pytest tests:")
print("1. Save the code above into a file named `test_my_math_pytest.py` (or similar).")
print("2. Make sure `unit_testing.py` (this file) is in the same directory or Python path.")
print("3. Open your terminal in that directory and run: `pytest`")
print("   Or `pytest -v` for more verbose output.")


print("\\n" + "-"*60 + "\\n")
print("--- 3. Mocking with `unittest.mock` ---")
# Mocking is used to replace parts of your system (like external dependencies, complex objects,
# or functions with side effects like API calls or database interactions) with mock objects.
# This allows you to test units of code in isolation.

# Example: Testing a function that makes an external API call.
class DataFetcher:
    def get_data_from_api(self, endpoint_url: str) -> dict:
        """Simulates fetching data from an external API."""
        # In a real scenario, this would use `requests.get(endpoint_url).json()` or similar
        print(f"  (Real DataFetcher: Making actual API call to {endpoint_url})")
        if endpoint_url == "https://api.example.com/user/1":
            return {"id": 1, "name": "Real User", "email": "real@example.com"}
        elif endpoint_url == "https://api.example.com/status":
            return {"status": "API is UP"}
        raise ConnectionError(f"Failed to connect to {endpoint_url}")

def process_user_data(fetcher_instance: DataFetcher, user_id: int) -> str:
    """Processes user data fetched from an API."""
    try:
        user_data = fetcher_instance.get_data_from_api(f"https://api.example.com/user/{user_id}")
        return f"User Name: {user_data['name']}, Email: {user_data['email']}"
    except ConnectionError:
        return "Could not fetch user data: API connection error."
    except KeyError:
        return "Could not fetch user data: Malformed API response."


class TestDataProcessing(unittest.TestCase):
    def test_process_user_data_success(self):
        """Test successful data processing using a mock."""
        # Create a mock DataFetcher instance
        mock_fetcher = MagicMock(spec=DataFetcher) # spec ensures mock has same interface

        # Configure the mock's get_data_from_api method to return a specific value
        mock_fetcher.get_data_from_api.return_value = {
            "id": 1, "name": "Mocked User", "email": "mocked@example.com"
        }

        result = process_user_data(mock_fetcher, user_id=1)

        # Assert that the mock method was called correctly
        mock_fetcher.get_data_from_api.assert_called_once_with("https://api.example.com/user/1")
        self.assertEqual(result, "User Name: Mocked User, Email: mocked@example.com")

    # Using @patch as a decorator to mock 'DataFetcher.get_data_from_api'
    # The mock object is passed as an argument to the test method.
    @patch('unit_testing.DataFetcher.get_data_from_api') # Path to the method to mock
    def test_process_user_data_connection_error_with_decorator(self, mock_get_data):
        """Test connection error handling using @patch decorator."""
        # Configure the mock to raise a ConnectionError when called
        mock_get_data.side_effect = ConnectionError("Simulated network failure.")

        # We need an instance of DataFetcher, but its method is mocked.
        # The mock is on the *class* DataFetcher's method, so any instance will use the mock.
        real_fetcher_instance_but_method_is_mocked = DataFetcher()
        result = process_user_data(real_fetcher_instance_but_method_is_mocked, user_id=2)

        mock_get_data.assert_called_once_with("https://api.example.com/user/2")
        self.assertEqual(result, "Could not fetch user data: API connection error.")

    def test_process_user_data_malformed_response_with_context_manager(self):
        """Test malformed API response using patch as a context manager."""
        with patch('unit_testing.DataFetcher.get_data_from_api') as mock_get_data:
            # Configure the mock for this specific 'with' block
            mock_get_data.return_value = {"id": 3, "username": "UnexpectedKey"} # Missing 'name' and 'email'

            real_fetcher_instance_but_method_is_mocked = DataFetcher()
            result = process_user_data(real_fetcher_instance_but_method_is_mocked, user_id=3)

            mock_get_data.assert_called_once_with("https://api.example.com/user/3")
            self.assertEqual(result, "Could not fetch user data: Malformed API response.")

# `unittest.mock.patch` can also be used as a decorator for a class, or to patch objects.
# `MagicMock` automatically creates mock attributes and methods as they are accessed.

print("\\n" + "-"*60 + "\\n")
# Interview Tip:
# - `unittest`: Know `TestCase`, `test_*` methods, `assertEqual`, `assertRaises`, `setUp/tearDown`, `setUpClass/tearDownClass`.
# - `pytest`: Simpler syntax, `assert` statement, fixtures (`@pytest.fixture`), parametrization (`@pytest.mark.parametrize`).
#   How to run pytest from CLI.
# - Mocking: Understand why and how to use `unittest.mock` (`patch`, `MagicMock`) to isolate tests
#   from external dependencies or complex parts of the system.
# - Test-Driven Development (TDD): Basic idea (write tests first, then code to make them pass).

# Common Interview Question:
# Q: How can you write a simple unit test in Python?
# A: Using `unittest`: Create a class that inherits from `unittest.TestCase`. Define methods
#    starting with `test_`. Inside these methods, use `self.assert...` methods
#    (e.g., `self.assertEqual(a, b)`, `self.assertTrue(x)`) to check conditions.
#    Run with `unittest.main()`.
#    Using `pytest`: Create a Python file (e.g., `test_mymodule.py`). Define functions
#    starting with `test_`. Inside these functions, use plain `assert` statements.
#    Run with `pytest` command in the terminal.
#
# Q: What is mocking and why is it useful in unit testing?
# A: Mocking is creating "fake" objects that simulate the behavior of real objects or dependencies
#    (like database connections, API calls, or complex classes). It's useful because:
#    1. Isolation: Allows testing a unit of code in isolation without relying on external systems
#       or complex dependencies.
#    2. Speed: Real external calls can be slow; mocks are fast.
#    3. Determinism: External systems can be unreliable or have changing data. Mocks provide
#       consistent behavior, making tests predictable.
#    4. Test Edge Cases: Easily simulate error conditions or specific responses from dependencies
#       that might be hard to reproduce with real systems.
#    Python's `unittest.mock` module (with `patch` and `MagicMock`) is commonly used.
#
# Q: What are fixtures in pytest?
# A: Fixtures are functions that provide a fixed baseline or setup for tests. They can set up
#    resources (like database connections, sample data) needed by one or more tests and can also
#    handle cleanup. Tests can request fixtures by naming them as input arguments.
#    Pytest's fixture system is more flexible and powerful than `unittest`'s `setUp/tearDown`.

# This ensures that unittest.main() runs only when the script is executed directly.
if __name__ == "__main__":
    print("\\n--- Running unittest tests defined in this file ---")
    # You can run tests selectively:
    # suite = unittest.TestSuite()
    # suite.addTest(TestMathFunctions('test_add_integers'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    unittest.main(verbosity=1) # verbosity=2 gives more detail
    # Note: pytest would typically be run from the command line and would discover
    # tests in this file as well if its naming conventions are followed for classes/functions.
    # However, unittest.main() will exit the script, so pytest auto-discovery might not
    # run other pytest-specific tests in this file if executed as `python unit_testing.py`.
    # Best practice is separate files for pytest tests (e.g., test_unit_testing.py).
"""