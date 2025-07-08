"""
# Real-world Project: CLI Todo App

# This project integrates various Python concepts into a simple CLI Todo App.

import sys

class TodoApp:
    def __init__(self):
        self.todos = []

    def add_todo(self, task):
        self.todos.append(task)
        print(f"Added: {task}")

    def list_todos(self):
        print("Todo List:")
        for i, task in enumerate(self.todos, start=1):
            print(f"{i}. {task}")

    def remove_todo(self, index):
        try:
            task = self.todos.pop(index - 1)
            print(f"Removed: {task}")
        except IndexError:
            print("Invalid index")

def main():
    app = TodoApp()
    while True:
        command = input("Enter command (add/list/remove/exit): ").strip().lower()
        if command == "add":
            task = input("Enter task: ").strip()
            app.add_todo(task)
        elif command == "list":
            app.list_todos()
        elif command == "remove":
            index = int(input("Enter task number to remove: ").strip())
            app.remove_todo(index)
        elif command == "exit":
            print("Exiting...")
            sys.exit()
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()

# Interview Tip:
# Be prepared to explain how this project integrates various Python concepts.

# Common Interview Question:
# How can you handle user input in a CLI application?
# Use the `input()` function to capture user input.
"""