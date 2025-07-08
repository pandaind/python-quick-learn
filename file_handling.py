"""
# File Handling

# File handling allows you to read, write, and manipulate files.

# Writing to a File
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# Reading from a File
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # Output: Hello, World!

# Appending to a File
with open("example.txt", "a") as file:
    file.write("\nAppended Text")

# Reading Line by Line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Interview Tip:
# Be prepared to explain the difference between `r`, `w`, `a`, and `r+` modes in file handling.

# Common Interview Question:
# How does the `with` statement help in file handling?
# The `with` statement ensures that the file is properly closed after its suite finishes, even if an exception is raised.
"""