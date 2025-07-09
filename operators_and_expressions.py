"""
# Operators and Expressions

# Operators are used to perform operations on variables and values.
# An expression is a combination of values, variables, and operators that Python evaluates to produce a value.

print("--- 1. Arithmetic Operators ---")
a = 10
b = 3
print(f"{a} + {b} = {a + b}")   # Addition
print(f"{a} - {b} = {a - b}")   # Subtraction
print(f"{a} * {b} = {a * b}")   # Multiplication
print(f"{a} / {b} = {a / b}")   # Division (results in a float)
print(f"{a} // {b} = {a // b}") # Floor Division (discards the fractional part)
print(f"{a} % {b} = {a % b}")   # Modulus (remainder of the division)
print(f"{a} ** {b} = {a ** b}") # Exponentiation (a to the power of b)

print("\\n" + "-"*60 + "\\n")
print("--- 2. Assignment Operators ---")
# Used to assign values to variables.
x = 5
print(f"Initial x: {x}")

x += 2  # Equivalent to x = x + 2
print(f"x += 2: {x}") # x is now 7

x -= 3  # Equivalent to x = x - 3
print(f"x -= 3: {x}") # x is now 4

x *= 4  # Equivalent to x = x * 4
print(f"x *= 4: {x}") # x is now 16

x /= 2  # Equivalent to x = x / 2
print(f"x /= 2: {x}") # x is now 8.0 (float)

x //= 3 # Equivalent to x = x // 3
print(f"x //= 3: {x}")# x is now 2.0

x **= 3 # Equivalent to x = x ** 3
print(f"x **= 3: {x}")# x is now 8.0

x %= 5  # Equivalent to x = x % 5
print(f"x %= 5: {x}") # x is now 3.0

# Other assignment operators exist for bitwise operations: &=, |=, ^=, >>=, <<=

print("\\n" + "-"*60 + "\\n")
print("--- 3. Comparison Operators ---")
# Used to compare two values. They return a Boolean value (True or False).
val1 = 10
val2 = 20
print(f"val1 = {val1}, val2 = {val2}")
print(f"{val1} == {val2}: {val1 == val2}") # Equal to
print(f"{val1} != {val2}: {val1 != val2}") # Not equal to
print(f"{val1} > {val2}: {val1 > val2}")   # Greater than
print(f"{val1} < {val2}: {val1 < val2}")   # Less than
print(f"{val1} >= {val2}: {val1 >= val2}") # Greater than or equal to
print(f"{val1} <= {val2}: {val1 <= val2}") # Less than or equal to

print("\\n" + "-"*60 + "\\n")
print("--- 4. Logical Operators ---")
# Used to combine conditional statements.
p = True
q = False
print(f"p = {p}, q = {q}")
print(f"p and q: {p and q}")  # Logical AND: True if both are true
print(f"p or q: {p or q}")   # Logical OR: True if at least one is true
print(f"not p: {not p}")      # Logical NOT: True if the operand is false, and vice-versa

# Short-circuiting:
# - `and`: if the first operand is False, the second is not evaluated.
# - `or`: if the first operand is True, the second is not evaluated.
def true_func():
    print("true_func() called")
    return True
def false_func():
    print("false_func() called")
    return False

print("\\nShort-circuiting examples:")
_ = false_func() and true_func() # true_func() will not be called
_ = true_func() or false_func()   # false_func() will not be called

print("\\n" + "-"*60 + "\\n")
print("--- 5. Identity Operators ---")
# Used to compare the memory locations of two objects.
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1: {list1}, id: {id(list1)}")
print(f"list2: {list2}, id: {id(list2)}")
print(f"list3: {list3}, id: {id(list3)}")

print(f"list1 is list2: {list1 is list2}")     # False, because list1 and list2 are different objects in memory, even if their content is the same.
print(f"list1 is list3: {list1 is list3}")     # True, because list3 refers to the exact same object as list1.
print(f"list1 is not list2: {list1 is not list2}") # True

# `is` vs `==`:
# `==` checks if the values of two operands are equal.
# `is` checks if two operands refer to the same object in memory.
print(f"list1 == list2: {list1 == list2}")     # True, because their contents are the same.

# For small integers and some strings, Python might cache them, so `is` might return True.
# This is an implementation detail and should not be relied upon for correctness for mutable objects or larger values.
num1 = 256
num2 = 256
print(f"num1 ({num1}) is num2 ({num2}): {num1 is num2}") # Often True due to caching for small integers

str1 = "hello"
str2 = "hello"
print(f"str1 ('{str1}') is str2 ('{str2}'): {str1 is str2}") # Often True due to string interning

print("\\n" + "-"*60 + "\\n")
print("--- 6. Membership Operators ---")
# Used to test if a sequence is presented in an object (e.g., lists, tuples, strings, sets, dictionaries (checks keys)).
my_list = [10, 20, 30, 40, 50]
my_string = "Hello Python"
my_dict = {"a": 1, "b": 2}

print(f"20 in my_list: {20 in my_list}")             # True
print(f"60 in my_list: {60 in my_list}")             # False
print(f"60 not in my_list: {60 not in my_list}")     # True

print(f"'H' in my_string: {'H' in my_string}")       # True
print(f"'Bye' in my_string: {'Bye' in my_string}")   # False

print(f"'a' in my_dict: {'a' in my_dict}")           # True (checks keys by default)
print(f"1 in my_dict.values(): {1 in my_dict.values()}") # True (checking if 1 is a value)


print("\\n" + "-"*60 + "\\n")
print("--- 7. Bitwise Operators ---")
# Used to perform operations on integers at the binary level.
# These are less common in general scripting but important in specific domains (e.g., low-level programming, image processing).
m = 60  # Binary: 0011 1100
n = 13  # Binary: 0000 1101
print(f"m = {m} (bin: {bin(m)}), n = {n} (bin: {bin(n)})")

print(f"m & n (AND): {m & n}")      # Bitwise AND (0000 1100 = 12)
                                    #  0011 1100
                                    #& 0000 1101
                                    #------------
                                    #  0000 1100 (12)

print(f"m | n (OR): {m | n}")       # Bitwise OR (0011 1101 = 61)
                                    #  0011 1100
                                    #| 0000 1101
                                    #------------
                                    #  0011 1101 (61)

print(f"m ^ n (XOR): {m ^ n}")      # Bitwise XOR (0011 0001 = 49)
                                    #  0011 1100
                                    #^ 0000 1101
                                    #------------
                                    #  0011 0001 (49)

print(f"~m (NOT/Complement): {~m}") # Bitwise NOT (inverts all bits). Result is -(m+1) for signed integers. (-61)
                                    # ~0011 1100 -> 1100 0011 (Two's complement representation for -61)

print(f"m << 2 (Left Shift): {m << 2}") # Left shift m by 2 bits (0011 1100 << 2 = 1111 0000 = 240). Equivalent to m * (2**2).
print(f"m >> 2 (Right Shift): {m >> 2}")# Right shift m by 2 bits (0011 1100 >> 2 = 0000 1111 = 15). Equivalent to m // (2**2).

print("\\n" + "-"*60 + "\\n")
print("--- 8. Walrus Operator (Assignment Expressions) ---")
# Introduced in Python 3.8 (PEP 572).
# Assigns a value to a variable as part of a larger expression.
# Syntax: `(name := expression)` - parentheses often needed.

# Example: Without walrus operator
# my_input = input("Enter something: ")
# while my_input != "quit":
#     print(f"You entered: {my_input}")
#     my_input = input("Enter something: ")

# Example: With walrus operator
# (This example is commented out to prevent blocking execution in non-interactive environments)
# print("Type 'quit' to exit the walrus demo loop.")
# while (command := input("Walrus Demo > ")) != "quit":
#     print(f"Command was: {command}")

# Another common use case: in comprehensions or if statements
numbers = [1, 2, 3, 4, 5, 6]
if (n := len(numbers)) > 5:
    print(f"List is too long (length {n})")

processed_values = [y for x in numbers if (y := x * 2) > 5]
print(f"Processed values > 5 (using walrus): {processed_values}")


print("\\n" + "-"*60 + "\\n")
print("--- 9. Operator Precedence and Associativity ---")
# Operator precedence determines the order in which operations are performed.
# For example, `*` and `/` have higher precedence than `+` and `-`.
# Associativity determines the order for operators with the same precedence (e.g., left-to-right for `+`, `-`).

# Example of precedence:
result_precedence = 10 + 5 * 2  # Multiplication (5*2=10) happens before addition (10+10=20)
print(f"10 + 5 * 2 = {result_precedence}") # Output: 20

# Use parentheses to override default precedence:
result_override = (10 + 5) * 2 # Addition (10+5=15) happens first, then multiplication (15*2=30)
print(f"(10 + 5) * 2 = {result_override}") # Output: 30

# Python's Precedence Order (Highest to Lowest, simplified):
# 1. `()`: Parentheses (grouping)
# 2. `f(args...)`, `x[index]`, `x.attribute`: Function calls, Slicing, Attribute reference
# 3. `**`: Exponentiation (right-associative)
# 4. `~x`, `+x`, `-x`: Bitwise NOT, Unary plus, Unary minus (positive/negative)
# 5. `*`, `/`, `//`, `%`: Multiplication, Division, Floor division, Modulus
# 6. `+`, `-`: Addition and Subtraction
# 7. `<<`, `>>`: Bitwise shifts
# 8. `&`: Bitwise AND
# 9. `^`: Bitwise XOR
# 10. `|`: Bitwise OR
# 11. `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==`: Comparisons, including membership and identity
# 12. `not x`: Logical NOT
# 13. `and`: Logical AND
# 14. `or`: Logical OR
# 15. `if-else` (conditional expression)
# 16. `lambda`: Lambda expression
# 17. `:=`: Assignment expression (Walrus operator)

# Full table: https://docs.python.org/3/reference/expressions.html#operator-precedence

# Interview Tip:
# - Be ready to explain operator precedence (e.g., `*` before `+`).
# - Understand the difference between `is` (identity) and `==` (equality). This is a very common question.
# - Know what membership operators (`in`, `not in`) do.
# - Basic understanding of bitwise operators can be a plus for certain roles.
# - Walrus operator (`:=`) is newer; knowing its basic use shows you're up-to-date.

# Common Interview Question:
# Q: What is the difference between `is` and `==` in Python?
# A: `==` (Equality): Checks if the values of two operands are equal.
#    `is` (Identity): Checks if two operands refer to the exact same object in memory (i.e., they have the same `id()`).
#    For immutable types like small integers or strings, Python might reuse objects, so `is` can sometimes
#    behave like `==`, but this is an implementation detail and shouldn't be relied upon for comparing values,
#    especially for mutable objects or larger/complex immutable objects. Always use `==` for value comparison.
"""