"""
# Working with External Libraries

# External libraries extend the functionality of Python. You can install them using pip (Python's package installer).

# -----------------------------------------------------------------------------
# 1. Virtual Environments
# -----------------------------------------------------------------------------
# Why use Virtual Environments?
# - Dependency Management: Different projects may require different versions of the same library.
#   Virtual environments allow you to install specific library versions for each project without conflicts.
# - Project Isolation: Keeps your global Python installation clean and organized. Dependencies for one
#   project don't interfere with another.
# - Reproducibility: Makes it easier to share projects and ensure others can set up the same environment
#   with the correct dependencies (often using a requirements.txt file).

# Common Tool: `venv` (built into Python 3.3+)
# (Older tool: `virtualenv` - still used, especially for Python 2 or specific features)

# Creating a Virtual Environment (using `venv`)
# Open your terminal or command prompt. Navigate to your project directory.
# Command: python -m venv <name_of_your_virtual_env>
# Example: python -m venv myenv
# This creates a directory (e.g., `myenv`) containing a copy of the Python interpreter and pip.
print("--- Virtual Environment Setup (Conceptual Commands) ---")
print("To create a venv (run in terminal):")
print("cd /path/to/your/project")
print("python -m venv venv_name  # Common name is 'venv' or '.venv'")

# Activating a Virtual Environment
# Activation scripts are inside the virtual environment directory (e.g., `myenv/Scripts` on Windows, `myenv/bin` on macOS/Linux).
# Windows: venv_name\\Scripts\\activate
# macOS/Linux: source venv_name/bin/activate
# Once activated, your terminal prompt usually changes to show the venv name.
# `pip` will now install packages into this environment.
print("\\nTo activate a venv (run in terminal):")
print("# On Windows:")
print("# venv_name\\Scripts\\activate")
print("# On macOS/Linux:")
print("# source venv_name/bin/activate")

# Deactivating a Virtual Environment
# Simply type `deactivate` in the terminal.
print("\\nTo deactivate a venv (run in terminal):")
print("# deactivate")

# -----------------------------------------------------------------------------
# 2. Installing Packages with `pip` (within an activated virtual environment)
# -----------------------------------------------------------------------------
# `pip` is the package installer for Python.
# Common pip commands:
# - `pip install <package_name>`: Installs the latest version of a package.
# - `pip install <package_name>==<version>`: Installs a specific version.
# - `pip install -r requirements.txt`: Installs all packages listed in a requirements file.
# - `pip list`: Lists installed packages in the current environment.
# - `pip freeze`: Outputs installed packages in requirements format (often used to create requirements.txt).
#   Example: `pip freeze > requirements.txt`
# - `pip uninstall <package_name>`: Uninstalls a package.
print("\\n--- Pip Usage (Conceptual Commands, run in activated venv terminal) ---")
print("pip install requests")
print("pip install numpy==1.20.0")
print("pip freeze > requirements.txt  # Save dependencies")
print("pip install -r requirements.txt # Install dependencies from file")
print("pip list")
print("pip uninstall requests")
print("-" * 50)

# -----------------------------------------------------------------------------
# 3. Example: Using the `requests` Library (after `pip install requests`)
# -----------------------------------------------------------------------------
# Ensure you have run `pip install requests` in your activated virtual environment first.
try:
    import requests
except ImportError:
    print("\\n** `requests` library not found. Please install it: `pip install requests` **\\n")
    requests = None # So the rest of the file doesn't break if not installed

if requests:
    print("\\n--- Example: Using `requests` library ---")
    try:
        response = requests.get("https://api.github.com")
        response.raise_for_status() # Raises an HTTPError for bad responses (4XX or 5XX)
        print(f"GitHub API Status Code: {response.status_code}")
        # .json() parses the JSON response into a Python dictionary
        print(f"GitHub API JSON Response (first few keys): {list(response.json().keys())[:5]}")
    except requests.exceptions.RequestException as e:
        print(f"Could not connect to GitHub API: {e}")
else:
    print("\\nSkipping `requests` example as the library is not available.")


# -----------------------------------------------------------------------------
# 4. Example: Using the `json` Library (built-in, no install needed)
# -----------------------------------------------------------------------------
# The `json` library is part of Python's standard library.
import json

print("\\n--- Example: Using `json` library (built-in) ---")

# The `json` library is part of Python's standard library.
# import json # Already imported above if requests was successfully imported, or imported standalone if not.
# We can ensure it's imported if not already:
if 'json' not in globals():
    import json

data = '{"name": "Alice", "age": 25}' # Original example data
parsed_data = json.loads(data)
print(f"Parsed JSON data: {parsed_data}")

# Interview Tip:
# Be prepared to explain how to install and use external libraries in Python, including virtual environments and pip.

# Common Interview Question:
# How can you parse a JSON string in Python?
# Use `json.loads(json_string)` to parse a JSON string.
"""