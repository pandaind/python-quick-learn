"""
# Working with External Libraries

# External libraries extend the functionality of Python. You can install them using pip.

# Using the `requests` Library
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())

# Using the `json` Library
import json

data = '{"name": "Alice", "age": 25}'
parsed_data = json.loads(data)
print(parsed_data)

# Interview Tip:
# Be prepared to explain how to install and use external libraries in Python.

# Common Interview Question:
# How can you parse a JSON string in Python?
# Use `json.loads(json_string)` to parse a JSON string.
"""