"""
# Regular Expressions

# Regular expressions are used to match patterns in strings.

import re

# Matching a Pattern
pattern = r"\d+"
text = "There are 123 apples"
match = re.search(pattern, text)
if match:
    print("Match found:", match.group())

# Finding All Matches
matches = re.findall(pattern, text)
print("All matches:", matches)

# Replacing a Pattern
new_text = re.sub(pattern, "many", text)
print("Replaced text:", new_text)

# Interview Tip:
# Be ready to explain the use cases for regular expressions.

# Common Interview Question:
# How can you use regular expressions to find all numbers in a string?
# Use `re.findall(r"\d+", string)` to find all numbers.
"""