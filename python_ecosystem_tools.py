"""
# Python Ecosystem: Style, Debugging, and Standard Library Highlights

# This file covers important aspects of the broader Python ecosystem that enhance
# code quality, development efficiency, and problem-solving capabilities.

import this # For PEP 20 - The Zen of Python
import os
import sys
import datetime
import time
import random
import collections
import itertools
# import pdb # pdb is typically used interactively, not usually imported directly like this for examples

print("--- 1. Python Enhancement Proposals (PEPs) ---")
# PEPs are design documents providing information to the Python community, or describing
# a new feature for Python or its processes or environment.

print("\\n--- 1.1 PEP 8: Style Guide for Python Code ---")
# PEP 8 is the official style guide for Python code. Adhering to it makes code more
# readable, consistent, and maintainable across different projects and developers.
# Key aspects include:
# - Indentation: Use 4 spaces per indentation level.
# - Line Length: Limit lines to 79 characters (docstrings/comments to 72).
# - Blank Lines: Use to separate logical sections, function/class definitions.
# - Imports: Group imports (standard library, then third-party, then local).
# - Naming Conventions:
#   - `lowercase` or `lower_case_with_underscores` for functions, methods, variables, modules.
#   - `UPPERCASE_WITH_UNDERSCORES` for constants.
#   - `CapWords` (CamelCase) for class names.
#   - `_leading_underscore`: Weak "internal use" indicator.
#   - `__leading_double_underscore`: Name mangling for class attributes.
#   - `__leading_and_trailing_double_underscore__`: "Magic" objects or attributes (e.g., `__init__`).
# - Comments: Write clear, concise comments. Use docstrings for modules, classes, functions, methods.
# - Whitespace: Use judiciously around operators and after commas.
#
# Tools like linters (e.g., Flake8, Pylint) and formatters (e.g., Black, autopep8)
# can help automatically check and enforce PEP 8 compliance.
print("PEP 8 provides guidelines for code layout, naming, comments, and more.")
print("Consistent style improves readability and collaboration.")
print("See the full PEP 8: https://www.python.org/dev/peps/pep-0008/")

print("\\n--- 1.2 PEP 20: The Zen of Python ---")
# PEP 20 is a collection of 19 guiding principles for Python's design, written by Tim Peters.
# It can be displayed by running `import this` in a Python interpreter.
print("The Zen of Python (PEP 20) by Tim Peters:")
# The `import this` statement itself prints The Zen of Python.
# We don't need to explicitly print it again if `import this` is above.
# If `import this` was not run, we could do:
# zen_lines = [
#     "Beautiful is better than ugly.", "Explicit is better than implicit.",
#     # ... and so on
# ]
# for line in zen_lines: print(f"  {line}")
print("  (The 'import this' statement at the top of this file already printed it.)")


print("\\n" + "-"*60 + "\\n")
print("--- 2. Debugging in Python ---")

print("\\n--- 2.1 Using `print()` statements (Basic Debugging) ---")
# The simplest form of debugging is inserting print statements to inspect variable values
# at different points in your code.
# Effective for simple cases but can become cumbersome for complex issues.
def faulty_function(a, b):
    print(f"  DEBUG: faulty_function received a={a}, b={b}")
    result = a * b # Intended a + b
    print(f"  DEBUG: faulty_function result before modification={result}")
    # ... more logic ...
    result = result + 5 # Further modification
    print(f"  DEBUG: faulty_function final result={result}")
    return result
print("Example of print() debugging (imagine 'a*b' should be 'a+b'):")
faulty_function(3, 4)


print("\\n--- 2.2 Python Debugger (`pdb`) ---")
# `pdb` is Python's built-in interactive debugger. It allows you to step through code,
# inspect variables, and set breakpoints.
#
# To use `pdb`:
# 1. Import it: `import pdb`
# 2. Set a breakpoint: `pdb.set_trace()` at the line where you want to start debugging.
#
# Common `pdb` commands (once `pdb.set_trace()` is hit and you're in the debugger):
#   - `n` (next): Execute the current line and go to the next line in the current function.
#   - `s` (step): Step into a function call.
#   - `c` (continue): Continue execution until the next breakpoint or the end of the script.
#   - `l` (list): List source code around the current line.
#   - `p <expression>` (print): Print the value of an expression (e.g., `p my_variable`).
#   - `pp <expression>` (pretty-print): Pretty-print the value of an expression.
#   - `w` (where): Print the current call stack.
#   - `a` (args): Print the arguments of the current function.
#   - `b <line_number>`: Set a breakpoint at a specific line number.
#   - `b <function_name>`: Set a breakpoint at the first line of a function.
#   - `cl <breakpoint_number>`: Clear a breakpoint.
#   - `q` (quit): Quit the debugger and exit the script.
#   - `h` (help): Show help for pdb commands. `h <command>` for specific command.
#
# Example (conceptual - running this script won't drop into pdb unless you uncomment `pdb.set_trace()`):
def pdb_example_function(x, y):
    z = x + y
    # import pdb; pdb.set_trace() # <--- Uncomment this line to activate pdb here
    # When execution reaches this line, the pdb debugger will start in your terminal.
    # You can then type commands like 'p z' or 'n'.
    result = z * 2
    return result

print("Conceptual pdb example: pdb_example_function(5, 10)")
# If you were to run with pdb.set_trace() uncommented, the script would pause here.
# result_pdb = pdb_example_function(5, 10)
# print(f"Result from (conceptual) pdb_example_function: {result_pdb}")
print("  (To try pdb, uncomment `import pdb; pdb.set_trace()` in `pdb_example_function` and run the script.)")

# Starting with Python 3.7, you can use the built-in `breakpoint()` function
# instead of `import pdb; pdb.set_trace()`. It's more flexible as it can be
# configured via an environment variable (PYTHONBREAKPOINT).
# def breakpoint_example_function(x, y):
#     z = x + y
#     breakpoint() # <--- Python 3.7+ way to enter debugger
#     result = z * 2
#     return result

print("\\n--- 2.3 IDE Debuggers ---")
# Most Integrated Development Environments (IDEs) like VS Code, PyCharm, Spyder, etc.,
# have powerful graphical debuggers.
# Features typically include:
# - Setting breakpoints visually by clicking in the margin.
# - Stepping through code (step over, step into, step out).
# - Inspecting variables and their current values in a dedicated panel.
# - Viewing the call stack.
# - Conditional breakpoints (break only if a certain condition is met).
# - Watch expressions (evaluate expressions continuously).
# IDE debuggers are often more user-friendly than `pdb` for complex debugging sessions.
print("IDEs (VS Code, PyCharm, etc.) offer powerful graphical debuggers.")
print("These are usually preferred for more complex debugging tasks.")


print("\\n" + "-"*60 + "\\n")
print("--- 3. Standard Library Highlights ---")
# Python has a rich standard library ("batteries included").
# Here are a few commonly used modules beyond the very basics like `math`.

print("\\n--- 3.1 `os` and `sys` - System Interaction ---")
# `os`: Interacting with the operating system (files, directories, processes).
print(f"Current working directory (os.getcwd()): {os.getcwd()}")
# os.makedirs("temp_dir/subdir", exist_ok=True) # Creates directories
# print(f"Files in current dir (os.listdir()): {os.listdir('.')[:5]}") # First 5 for brevity
# file_path = os.path.join("temp_dir", "my_file.txt") # OS-independent path joining
# print(f"Constructed path (os.path.join): {file_path}")

# `sys`: Access to system-specific parameters and functions (interpreter related).
print(f"Python version (sys.version): {sys.version.split()[0]}")
print(f"Platform (sys.platform): {sys.platform}")
# print(f"Command line arguments (sys.argv): {sys.argv}") # sys.argv[0] is script name
# sys.exit(0) # Exit the script

print("\\n--- 3.2 `datetime` and `time` - Date and Time ---")
# `datetime`: Classes for manipulating dates and times.
now = datetime.datetime.now()
today = datetime.date.today()
print(f"Current datetime (datetime.now()): {now}")
print(f"Today's date (date.today()): {today}")
print(f"Formatted datetime (strftime): {now.strftime('%Y-%m-%d %H:%M:%S')}")
specific_date = datetime.datetime(2024, 1, 1, 12, 30, 0)
print(f"Specific date: {specific_date}")
time_delta = datetime.timedelta(days=5, hours=3)
future_date = now + time_delta
print(f"5 days and 3 hours from now: {future_date}")

# `time`: Time-related functions, including `time.sleep()`.
# print("Pausing for 0.1 seconds using time.sleep(0.1)...")
# time.sleep(0.1) # Pause execution
# print(f"Current timestamp (time.time()): {time.time()}") # Seconds since epoch

print("\\n--- 3.3 `random` - Random Number Generation ---")
# `random`: Generating pseudo-random numbers.
print(f"Random float between 0.0 and 1.0 (random.random()): {random.random()}")
print(f"Random integer between 1 and 10 (random.randint(1,10)): {random.randint(1, 10)}")
my_items = ["rock", "paper", "scissors"]
print(f"Random choice from list (random.choice()): {random.choice(my_items)}")
deck = list(range(1, 53))
random.shuffle(deck) # Shuffles the list in-place
print(f"Shuffled deck (first 5): {deck[:5]}")

print("\\n--- 3.4 `collections` - Specialized Collection Datatypes ---")
# `collections`: Provides alternatives to Python's general purpose built-in containers.
# - `collections.Counter`: Dict subclass for counting hashable objects.
word_list = "apple banana apple orange banana apple".split()
word_counts = collections.Counter(word_list)
print(f"Word counts (Counter): {word_counts}") # Counter({'apple': 3, 'banana': 2, 'orange': 1})
print(f"Most common word: {word_counts.most_common(1)}") # [('apple', 3)]

# - `collections.defaultdict`: Dict subclass that calls a factory function to supply missing values.
#   Useful for grouping items.
dd = collections.defaultdict(list) # Default factory is list (creates empty list for missing key)
pairs = [('a', 1), ('b', 2), ('a', 3), ('c', 4), ('b', 5)]
for key, value in pairs:
    dd[key].append(value)
print(f"Grouped items (defaultdict(list)): {dd}") # defaultdict(<class 'list'>, {'a': [1, 3], 'b': [2, 5], 'c': [4]})

# - `collections.namedtuple`: Factory function for creating tuple subclasses with named fields.
Point = collections.namedtuple('Point', ['x', 'y', 'z'])
p1 = Point(10, 20, 30)
print(f"Named tuple Point: {p1}, x={p1.x}, y={p1.y}, z={p1.z}")

# - `collections.deque`: List-like container with fast appends and pops on either end.
#   (Already shown in built_in_data_structures.py for Queue implementation)
dq = collections.deque([1,2,3])
dq.appendleft(0)
dq.append(4)
print(f"Deque: {dq}") # deque([0, 1, 2, 3, 4])
dq.popleft()
print(f"Deque after popleft: {dq}") # deque([1, 2, 3, 4])


print("\\n--- 3.5 `itertools` - Functions Creating Iterators for Efficient Looping ---")
# `itertools`: Provides functions for creating iterators for efficient looping.
# Many useful functions for permutations, combinations, infinite iterators, etc.
# Example: `itertools.cycle` (infinite iterator)
# colors_cycle = itertools.cycle(['red', 'green', 'blue'])
# print("First 5 from itertools.cycle(['red', 'green', 'blue']):")
# for _ in range(5):
#     print(next(colors_cycle)) # red, green, blue, red, green

# Example: `itertools.permutations`
perms = itertools.permutations('ABC', 2) # Permutations of length 2
print(f"Permutations of 'ABC' taken 2 at a time: {list(perms)}")
# Output: [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# Example: `itertools.combinations`
combs = itertools.combinations('ABC', 2) # Combinations of length 2
print(f"Combinations of 'ABC' taken 2 at a time: {list(combs)}")
# Output: [('A', 'B'), ('A', 'C'), ('B', 'C')]

# Example: `itertools.product` (Cartesian product)
prod = itertools.product('AB', '12')
print(f"Cartesian product of 'AB' and '12': {list(prod)}")
# Output: [('A', '1'), ('A', '2'), ('B', '1'), ('B', '2')]


print("\\nMany other useful modules exist in the standard library, such as:")
print("- `json`: For working with JSON data.")
print("- `re`: For regular expressions.")
print("- `unittest` or `pytest` (pytest is third-party but very common): For testing.")
print("- `logging`: For flexible event logging.")
print("- `argparse`: For parsing command-line arguments.")
print("- `http.server`, `socket`: For networking.")
print("- `sqlite3`: For SQLite database interaction.")
print("Exploring the Python Standard Library documentation is highly recommended!")

print("\\n" + "-"*60 + "\\n")
# Interview Tip:
# - Know PEP 8 and PEP 20 (The Zen of Python) by name and their general purpose.
# - Be able to describe basic debugging techniques (print statements, `pdb` or IDE debugger).
# - Be familiar with some key standard library modules and their use cases (e.g., `os`, `sys`,
#   `datetime`, `random`, `collections`, `itertools`, `json`, `re`). You don't need to know
#   every function, but understanding what kind of tasks these modules help with is important.
"""
