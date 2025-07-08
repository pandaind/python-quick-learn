"""
# Loops

# Loops are used to execute a block of code repeatedly.

# For Loop
for i in range(5):
    print(i)

# While Loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop Control Statements
# Break: Exit the loop
# Continue: Skip the current iteration
# Pass: Do nothing

for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 3:
        continue
    print(i)

# Interview Tip:
# Be ready to explain the difference between `for` and `while` loops.

# Common Interview Question:
# How can you iterate over a list using a loop in Python?
# You can use a `for` loop to iterate over a list.
"""