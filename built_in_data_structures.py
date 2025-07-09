"""
# Python's Built-in Data Structures

# This file provides a comprehensive overview of Python's core built-in data structures.
# These are fundamental tools for any Python programmer.

# -----------------------------------------------------------------------------
# 1. Lists
# -----------------------------------------------------------------------------
# - Ordered: Elements are stored in a specific sequence.
# - Mutable: Elements can be changed after the list is created (added, removed, modified).
# - Allows Duplicates: A list can contain multiple occurrences of the same element.
# - Heterogeneous: Can store elements of different data types (though often homogeneous for clarity).

# Creating Lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]
list_from_iterable = list("python") # Creates ['p', 'y', 't', 'h', 'o', 'n']

print(f"Empty list: {empty_list}")
print(f"Numbers list: {numbers}")
print(f"Mixed list: {mixed_list}")
print(f"List from iterable: {list_from_iterable}")

# Accessing Elements (Indexing)
# Zero-based indexing
fruits = ["apple", "banana", "cherry", "date"]
print(f"First fruit: {fruits[0]}")   # Output: apple
print(f"Last fruit: {fruits[-1]}")  # Output: date (negative indexing)
# print(fruits[4]) # Raises IndexError

# Slicing Lists
# slice_object = slice(start, stop, step)
# list[start:stop:step]
print(f"First two fruits: {fruits[0:2]}")      # Output: ['apple', 'banana']
print(f"Fruits from index 1: {fruits[1:]}")     # Output: ['banana', 'cherry', 'date']
print(f"Fruits up to index 2 (exclusive): {fruits[:2]}") # Output: ['apple', 'banana']
print(f"Every other fruit: {fruits[::2]}")      # Output: ['apple', 'cherry']
print(f"Reverse the list: {fruits[::-1]}")      # Output: ['date', 'cherry', 'banana', 'apple']

# Modifying Lists
fruits[1] = "blueberry"
print(f"Fruits after modification: {fruits}") # Output: ['apple', 'blueberry', 'cherry', 'date']

# Common List Methods

# append(element): Adds an element to the end of the list.
fruits.append("elderberry")
print(f"After append: {fruits}") # Output: ['apple', 'blueberry', 'cherry', 'date', 'elderberry']

# extend(iterable): Extends the list by appending all items from an iterable.
more_fruits = ["fig", "grape"]
fruits.extend(more_fruits)
print(f"After extend: {fruits}") # Output: ['apple', 'blueberry', 'cherry', 'date', 'elderberry', 'fig', 'grape']

# insert(index, element): Inserts an element at a specific position.
fruits.insert(1, "apricot")
print(f"After insert: {fruits}") # Output: ['apple', 'apricot', 'blueberry', 'cherry', 'date', 'elderberry', 'fig', 'grape']

# remove(element): Removes the first occurrence of an element. Raises ValueError if not found.
fruits.remove("cherry")
print(f"After remove 'cherry': {fruits}")
# fruits.remove("kiwi") # Raises ValueError

# pop(index=-1): Removes and returns the element at a specific position (default is the last).
popped_fruit = fruits.pop()
print(f"Popped fruit (last): {popped_fruit}, List now: {fruits}")
popped_fruit_at_index = fruits.pop(2) # Removes 'blueberry'
print(f"Popped fruit (index 2): {popped_fruit_at_index}, List now: {fruits}")

# clear(): Removes all elements from the list.
temp_list = [1, 2, 3]
temp_list.clear()
print(f"Cleared list: {temp_list}") # Output: []

# index(element, start=0, end=len(list)): Returns the index of the first occurrence of an element.
# Raises ValueError if not found.
print(f"Index of 'date': {fruits.index('date')}")

# count(element): Returns the number of times an element appears in the list.
numbers_with_duplicates = [1, 2, 2, 3, 2, 4]
print(f"Count of 2: {numbers_with_duplicates.count(2)}") # Output: 3

# sort(key=None, reverse=False): Sorts the list in-place.
# Can sort numbers or strings. For mixed types, it will raise TypeError unless a key is provided.
unsorted_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
unsorted_numbers.sort()
print(f"Sorted numbers: {unsorted_numbers}")
unsorted_numbers.sort(reverse=True)
print(f"Sorted numbers (descending): {unsorted_numbers}")

unsorted_fruits = ["date", "apple", "cherry"]
unsorted_fruits.sort()
print(f"Sorted fruits: {unsorted_fruits}")

# Sorting with a key (e.g., by length of string)
unsorted_fruits.sort(key=len)
print(f"Fruits sorted by length: {unsorted_fruits}")

# sorted() built-in function: Returns a new sorted list, doesn't modify original.
original_numbers = [3, 1, 4]
new_sorted_list = sorted(original_numbers)
print(f"Original numbers: {original_numbers}, New sorted list: {new_sorted_list}")

# reverse(): Reverses the elements of the list in-place.
fruits.reverse()
print(f"Reversed fruits: {fruits}")

# Copying Lists
# Assignment creates a reference, not a copy
list_a = [1, 2, 3]
list_b = list_a
list_b.append(4)
print(f"List A after modifying B: {list_a}") # Output: [1, 2, 3, 4] (A is affected)

# Shallow Copy (copies top-level elements, nested structures are still references)
# Using slicing
list_c = list_a[:]
list_c.append(5)
print(f"List A: {list_a}, List C (shallow copy): {list_c}")
# If list_a contained mutable nested lists, changes to those nested lists in list_c would affect list_a.

# Using copy() method
list_d = list_a.copy()
list_d.append(6)
print(f"List A: {list_a}, List D (shallow copy): {list_d}")

# Example of shallow copy issue with nested lists
nested_list_original = [1, [2, 3]]
nested_list_shallow_copy = nested_list_original.copy()
nested_list_shallow_copy[0] = 100        # Original not affected
nested_list_shallow_copy[1].append(4)  # Original's nested list IS affected
print(f"Original nested list: {nested_list_original}") # Output: [1, [2, 3, 4]]
print(f"Shallow copy nested list: {nested_list_shallow_copy}") # Output: [100, [2, 3, 4]]

# Deep Copy (copies all elements, including nested structures, recursively)
import copy
nested_list_original_2 = [1, [2, 3]]
nested_list_deep_copy = copy.deepcopy(nested_list_original_2)
nested_list_deep_copy[0] = 200
nested_list_deep_copy[1].append(5)
print(f"Original nested list 2: {nested_list_original_2}") # Output: [1, [2, 3]] (unaffected)
print(f"Deep copy nested list: {nested_list_deep_copy}") # Output: [200, [2, 3, 5]]

# List Comprehensions (briefly here; for a more detailed explanation of comprehensions, see comprehensions.py)
squares = [x**2 for x in range(10)]
print(f"Squares using list comprehension: {squares}")
even_numbers = [x for x in range(20) if x % 2 == 0]
print(f"Even numbers using list comprehension: {even_numbers}")

# Common Interview Questions/Tips for Lists:
# - Time complexity of operations (append is O(1) on average, insert/delete can be O(n), search is O(n)).
# - Difference between sort() method and sorted() function.
# - Shallow vs. Deep copy.
# - How lists are stored in memory (dynamic arrays).
# - When to use a list vs. a tuple.

print("\\n" + "-"*60 + "\\n") # Separator for next section

# -----------------------------------------------------------------------------
# 2. Tuples
# -----------------------------------------------------------------------------
# - Ordered: Elements are stored in a specific sequence.
# - Immutable: Elements cannot be changed after the tuple is created.
# - Allows Duplicates: A tuple can contain multiple occurrences of the same element.
# - Heterogeneous: Can store elements of different data types.

# Creating Tuples
empty_tuple = ()
single_element_tuple = (1,) # Comma is crucial for single element tuple
# single_element_not_a_tuple = (1) # This would be an integer
numbers_tuple = (1, 2, 3, 4, 5)
mixed_tuple = (1, "hello", 3.14, True)
tuple_from_iterable = tuple("python") # Creates ('p', 'y', 't', 'h', 'o', 'n')
implicit_tuple = 10, 20, 30 # Tuple packing

print(f"Empty tuple: {empty_tuple}")
print(f"Single element tuple: {single_element_tuple}, type: {type(single_element_tuple)}")
print(f"Numbers tuple: {numbers_tuple}")
print(f"Mixed tuple: {mixed_tuple}")
print(f"Tuple from iterable: {tuple_from_iterable}")
print(f"Implicit tuple: {implicit_tuple}, type: {type(implicit_tuple)}")

# Accessing Elements (Indexing) - Same as lists
print(f"First element of numbers_tuple: {numbers_tuple[0]}")
print(f"Last element of mixed_tuple: {mixed_tuple[-1]}")

# Slicing Tuples - Same as lists, returns a new tuple
print(f"Slice of numbers_tuple: {numbers_tuple[1:3]}") # Output: (2, 3)
print(f"Reversed mixed_tuple: {mixed_tuple[::-1]}")

# Immutability - Tuples cannot be changed after creation
# numbers_tuple[0] = 100 # This would raise a TypeError
# numbers_tuple.append(6) # AttributeError: 'tuple' object has no attribute 'append'

# However, if a tuple contains mutable elements (like a list), the mutable element itself can be changed.
mutable_in_tuple = ([1, 2], 3)
mutable_in_tuple[0].append(30)
print(f"Tuple with modified mutable element: {mutable_in_tuple}") # Output: ([1, 2, 30], 3)

# Tuple Methods (Fewer than lists due to immutability)

# count(element): Returns the number of times an element appears in the tuple.
repeated_tuple = (1, 2, 2, 3, 2, 4)
print(f"Count of 2 in repeated_tuple: {repeated_tuple.count(2)}") # Output: 3

# index(element, start=0, end=len(tuple)): Returns the index of the first occurrence of an element.
# Raises ValueError if not found.
print(f"Index of 'hello' in mixed_tuple: {mixed_tuple.index('hello')}")

# Tuple Packing and Unpacking
# Packing: Assigning multiple values to a single tuple variable
packed_coordinates = 10, 20, 30 # x, y, z

# Unpacking: Assigning elements of a tuple to multiple variables
x, y, z = packed_coordinates
print(f"Unpacked coordinates: x={x}, y={y}, z={z}")

# Using * for extended unpacking (Python 3.x)
first, *rest, last = (10, 20, 30, 40, 50)
print(f"First: {first}, Rest: {rest}, Last: {last}") # Output: First: 10, Rest: [20, 30, 40], Last: 50

# Use Cases for Tuples:
# - Representing fixed collections of items (e.g., coordinates, RGB colors).
# - Dictionary keys (since they are immutable and hashable).
# - Returning multiple values from a function.
# - When you want to ensure data integrity (immutability).
# - Can sometimes be more memory efficient than lists for the same data.

def get_coordinates():
    return 10, 20 # Implicitly returns a tuple

coords = get_coordinates()
print(f"Coordinates from function: {coords}")

# Common Interview Questions/Tips for Tuples:
# - Key difference: mutability (list) vs. immutability (tuple).
# - When to use a tuple over a list.
# - Tuple packing and unpacking.
# - "Hashable" concept: Tuples containing only immutable elements are hashable and can be dictionary keys.
# - Single element tuple syntax (the trailing comma).

print("\\n" + "-"*60 + "\\n") # Separator for next section

# -----------------------------------------------------------------------------
# 3. Dictionaries (dict)
# -----------------------------------------------------------------------------
# - Unordered (Python < 3.7) / Ordered (Python 3.7+): Keys are stored in insertion order from Python 3.7.
# - Mutable: Can be changed after creation (add, remove, modify key-value pairs).
# - Key-Value Pairs: Stores data as key-value pairs.
# - Keys must be Immutable and Unique: Keys must be of a hashable type (e.g., string, number, tuple with immutable elements). Duplicate keys are not allowed (last one wins).
# - Values can be of any type and can be duplicated.

# Creating Dictionaries
empty_dict = {}
student = {
    "name": "Alice",
    "age": 25,
    "courses": ["Math", "Physics"]
}
dict_from_func = dict(name="Bob", age=30) # Using dict() constructor
dict_from_tuples = dict([('a', 1), ('b', 2)])

print(f"Empty dictionary: {empty_dict}")
print(f"Student dictionary: {student}")
print(f"Dict from func: {dict_from_func}")
print(f"Dict from tuples: {dict_from_tuples}")

# Accessing Elements
print(f"Student's name: {student['name']}")  # Using keys, raises KeyError if key not found
# print(student['grade']) # Raises KeyError

# Using get() method (safer, returns None or a default value if key not found)
print(f"Student's age: {student.get('age')}")
print(f"Student's grade (with get): {student.get('grade')}") # Output: None
print(f"Student's grade (with get and default): {student.get('grade', 'N/A')}") # Output: N/A

# Adding or Modifying Elements
student['age'] = 26  # Modify existing value
student['city'] = "New York" # Add new key-value pair
print(f"Student dict after modification/addition: {student}")

# Removing Elements
# pop(key, default): Removes the key and returns its value. Raises KeyError if key not found and no default.
removed_city = student.pop('city')
print(f"Removed city: {removed_city}, Student dict: {student}")
# removed_country = student.pop('country') # Raises KeyError
removed_country_safe = student.pop('country', 'Not Specified')
print(f"Removed country (safe): {removed_country_safe}")

# popitem(): Removes and returns an arbitrary (key, value) pair (LIFO from Python 3.7+).
# Raises KeyError if the dictionary is empty.
last_item = student.popitem() # In 3.7+, this would be the last inserted item not explicitly popped
print(f"Popped item: {last_item}, Student dict: {student}")
student['courses'] = ["Math", "Physics"] # Re-add for next examples
student['age'] = 26

# del keyword: Can remove a key-value pair or the entire dictionary.
temp_dict = {"a": 1, "b": 2}
del temp_dict['a']
print(f"Temp dict after del 'a': {temp_dict}")
# del temp_dict # Deletes the entire dictionary object

# clear(): Removes all items from the dictionary.
temp_dict.clear()
print(f"Cleared temp_dict: {temp_dict}")

# Dictionary Methods

# keys(): Returns a view object that displays a list of all the keys.
print(f"Student keys: {student.keys()}") # Output: dict_keys(['name', 'age', 'courses'])

# values(): Returns a view object that displays a list of all the values.
print(f"Student values: {student.values()}") # Output: dict_values(['Alice', 26, ['Math', 'Physics']])

# items(): Returns a view object that displays a list of a dictionary's key-value tuple pairs.
print(f"Student items: {student.items()}") # Output: dict_items([('name', 'Alice'), ('age', 26), ('courses', ['Math', 'Physics'])])

# View objects are dynamic and reflect changes in the dictionary.
student_keys_view = student.keys()
print(f"Keys before adding major: {student_keys_view}")
student['major'] = "Computer Science"
print(f"Keys after adding major (view updates): {student_keys_view}")
del student['major'] # Clean up

# update(other_dict or iterable of key-value pairs): Updates the dictionary with elements from another.
# Overwrites existing keys.
student.update({"age": 27, "country": "USA"})
print(f"Student after update: {student}")

# setdefault(key, default_value): Returns the value of a key. If key does not exist, inserts key with default_value.
major = student.setdefault('major', 'Undeclared')
print(f"Major (setdefault new): {major}, Student: {student}")
name = student.setdefault('name', 'Unknown') # Key 'name' exists
print(f"Name (setdefault existing): {name}, Student: {student}")

# Iterating Through Dictionaries
print("\\nIterating through student dictionary:")
# Iterate over keys (default iteration)
for key in student:
    print(f"Key: {key}, Value: {student[key]}")

# Iterate over values
for value in student.values():
    print(f"Value: {value}")

# Iterate over key-value pairs
for key, value in student.items():
    print(f"Key: {key} => Value: {value}")

# Dictionary Comprehensions (briefly here; for a more detailed explanation of comprehensions, see comprehensions.py)
squared_numbers_dict = {x: x**2 for x in range(1, 6)}
print(f"Squared numbers dict: {squared_numbers_dict}")

# Common Interview Questions/Tips for Dictionaries:
# - Time complexity: Average O(1) for insertion, deletion, and access. Worst case O(n).
# - Keys must be hashable. Why? (For efficient lookup using hash tables).
# - Difference between accessing with `[]` and `get()`.
# - Ordered vs. Unordered nature (Python 3.7+ guarantees insertion order).
# - View objects (`keys()`, `values()`, `items()`) are dynamic.
# - How to merge dictionaries (e.g., `update()`, `**` unpacking in Python 3.5+).
#   Example of `**` unpacking for merging:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict_unpack = {**dict1, **dict2} # dict2's 'b' overwrites dict1's 'b'
print(f"Merged with unpacking: {merged_dict_unpack}")


print("\\n" + "-"*60 + "\\n") # Separator for next section

# -----------------------------------------------------------------------------
# 4. Sets (set)
# -----------------------------------------------------------------------------
# - Unordered: Elements are not stored in any particular order. (Order may appear consistent in CPython for small sets, but not guaranteed).
# - Mutable: Sets themselves are mutable (can add/remove elements).
# - No Duplicate Elements: Each element in a set must be unique. Duplicates are automatically removed.
# - Elements must be Immutable: Elements added to a set must be of an immutable (hashable) type. (e.g., numbers, strings, tuples of immutables). You cannot have a list or another set as an element of a set.

# Creating Sets
empty_set = set() # Using set() is necessary for an empty set; {} creates an empty dictionary.
numbers_set = {1, 2, 3, 4, 5}
mixed_set_elements = {1, "hello", 3.14, ("a", "b")} # Tuple is immutable
set_from_list = set([1, 2, 2, 3, 4, 4, 4]) # Duplicates are removed
set_from_string = set("hello") # Creates {'h', 'e', 'l', 'o'}

print(f"Empty set: {empty_set}")
print(f"Numbers set: {numbers_set}")
print(f"Set from list (duplicates removed): {set_from_list}")
print(f"Set from string: {set_from_string}")
# invalid_set = {[1,2], 3} # This would raise a TypeError because list is mutable

# Set Methods

# add(element): Adds an element to the set. If already present, does nothing.
numbers_set.add(6)
numbers_set.add(3) # Adding an existing element
print(f"Numbers set after add: {numbers_set}")

# remove(element): Removes an element from the set. Raises KeyError if the element is not found.
numbers_set.remove(6)
print(f"Numbers set after remove(6): {numbers_set}")
# numbers_set.remove(10) # Raises KeyError

# discard(element): Removes an element from the set if it is present. Does not raise an error if not found.
numbers_set.discard(5)
numbers_set.discard(10) # No error
print(f"Numbers set after discard(5) and discard(10): {numbers_set}")

# pop(): Removes and returns an arbitrary element from the set. Raises KeyError if the set is empty.
# Since sets are unordered, you can't predict which element will be popped.
if numbers_set: # Check if set is not empty before popping
    popped_element = numbers_set.pop()
    print(f"Popped element: {popped_element}, Set now: {numbers_set}")

# clear(): Removes all elements from the set.
temp_set = {10, 20}
temp_set.clear()
print(f"Cleared set: {temp_set}")

# Set Operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Union: Returns a new set containing all items from both sets.
# Using | operator
union_set_op = set_a | set_b
print(f"Union (operator |): {union_set_op}")
# Using union() method
union_set_method = set_a.union(set_b) # or set_b.union(set_a)
print(f"Union (method union()): {union_set_method}")

# Intersection: Returns a new set containing only items present in both sets.
# Using & operator
intersection_set_op = set_a & set_b
print(f"Intersection (operator &): {intersection_set_op}")
# Using intersection() method
intersection_set_method = set_a.intersection(set_b)
print(f"Intersection (method intersection()): {intersection_set_method}")

# Difference: Returns a new set containing items from the first set that are not in the second set.
# Order matters.
# Using - operator
difference_set_ab_op = set_a - set_b # Elements in A but not in B
print(f"Difference A-B (operator -): {difference_set_ab_op}")
difference_set_ba_op = set_b - set_a # Elements in B but not in A
print(f"Difference B-A (operator -): {difference_set_ba_op}")
# Using difference() method
difference_set_ab_method = set_a.difference(set_b)
print(f"Difference A-B (method difference()): {difference_set_ab_method}")

# Symmetric Difference: Returns a new set containing all items from both sets except those that are common to both.
# (Items in A or B, but not in both)
# Using ^ operator
symmetric_diff_op = set_a ^ set_b
print(f"Symmetric Difference (operator ^): {symmetric_diff_op}")
# Using symmetric_difference() method
symmetric_diff_method = set_a.symmetric_difference(set_b)
print(f"Symmetric Difference (method symmetric_difference()): {symmetric_diff_method}")

# Subset and Superset
set_c = {1, 2}
print(f"Set C: {set_c}")
# issubset(): Returns True if another set contains this set.
print(f"Is C a subset of A? {set_c.issubset(set_a)}")   # True
print(f"Is A a subset of C? {set_a.issubset(set_c)}")   # False

# issuperset(): Returns True if this set contains another set.
print(f"Is A a superset of C? {set_a.issuperset(set_c)}") # True
print(f"Is C a superset of A? {set_c.issuperset(set_a)}") # False

# isdisjoint(): Returns True if two sets have no elements in common.
set_d = {7, 8}
print(f"Set D: {set_d}")
print(f"Are A and B disjoint? {set_a.isdisjoint(set_b)}") # False (common elements 3, 4)
print(f"Are A and D disjoint? {set_a.isdisjoint(set_d)}") # True

# In-place (mutating) versions of set operations:
# update() or |= (union update)
# intersection_update() or &=
# difference_update() or -=
# symmetric_difference_update() or ^=
set_a_copy = set_a.copy()
set_a_copy.update(set_b) # set_a_copy |= set_b
print(f"Set A after update with B: {set_a_copy}")

# Frozenset: An immutable version of a set.
# Once created, elements cannot be added or removed.
# Frozensets are hashable and can be used as dictionary keys or elements of another set.
frozen = frozenset([1, 2, 3, 3])
print(f"Frozenset: {frozen}")
# frozen.add(4) # AttributeError: 'frozenset' object has no attribute 'add'
# Can be a dictionary key:
dict_with_frozenset_key = {frozen: "my_frozen_set_data"}
print(f"Dict with frozenset key: {dict_with_frozenset_key}")

# Set Comprehensions (briefly here; for a more detailed explanation of comprehensions, see comprehensions.py)
squared_evens_set = {x**2 for x in range(10) if x % 2 == 0}
print(f"Squared evens set: {squared_evens_set}")

# Common Interview Questions/Tips for Sets:
# - Use cases: Removing duplicates from a list, membership testing (very fast - O(1) on average).
# - Difference between `remove()` and `discard()`.
# - Set operations and their corresponding operators/methods.
# - Elements must be hashable/immutable.
# - How to create an empty set ( `set()` not `{}` ).
# - Frozenset for when you need an immutable set.

print("\\n" + "-"*60 + "\\n") # Separator for next section

# -----------------------------------------------------------------------------
# 5. Strings (str) - As a Data Structure/Sequence
# -----------------------------------------------------------------------------
# - Ordered Sequence of Characters: Each character has a specific position (index).
# - Immutable: Strings cannot be changed after creation. Operations that seem to modify strings actually create new strings.
# - Unicode Support: Python strings handle Unicode characters.

# Creating Strings
empty_string = ""
single_quote_str = 'hello'
double_quote_str = "world"
multiline_str = """This is a
multiline string."""
str_from_num = str(123)

print(f"Empty string: '{empty_string}'")
print(f"Single quote string: {single_quote_str}")
print(f"Double quote string: {double_quote_str}")
print(f"Multiline string:\\n{multiline_str}")
print(f"String from number: {str_from_num}, type: {type(str_from_num)}")

# Accessing Characters (Indexing) - Same as lists/tuples
message = "Python is fun!"
print(f"First character: {message[0]}")  # Output: P
print(f"Last character: {message[-1]}") # Output: !

# Slicing Strings - Same as lists/tuples, returns a new string
print(f"Slice (Python): {message[0:6]}")   # Output: Python
print(f"Slice (fun!): {message[-4:]}")    # Output: fun!
print(f"Reversed message: {message[::-1]}") # Output: !nuf si nohtyP

# Immutability
# message[0] = "J" # This would raise a TypeError

# Common String Methods (Many more exist, these are some common ones for structure/querying)

# len(): Built-in function to get length of string (number of characters)
print(f"Length of message: {len(message)}")

# Concatenation (+) and Repetition (*)
greeting = "Hello"
name = "World"
combined = greeting + ", " + name + "!"
print(f"Combined string: {combined}")
repeated = "Echo... " * 3
print(f"Repeated string: {repeated}")

# Membership testing (in, not in)
print(f"'Python' in message? {'Python' in message}") # True
print(f"'Java' not in message? {'Java' not in message}") # True

# strip(), lstrip(), rstrip(): Remove whitespace (or specified characters) from ends.
padded_str = "   some text   "
print(f"Stripped: '{padded_str.strip()}'")
print(f"Left stripped: '{padded_str.lstrip()}'")
print(f"Right stripped: '{padded_str.rstrip()}'")
char_padded_str = "---text---"
print(f"Stripped with '-': '{char_padded_str.strip('-')}'")

# split(separator=None, maxsplit=-1): Splits the string into a list of substrings.
# Default separator is any whitespace.
words = message.split() # Splits by space
print(f"Words from message: {words}")
csv_data = "apple,banana,cherry"
fruits_list = csv_data.split(',')
print(f"Fruits from CSV: {fruits_list}")

# join(iterable): Joins elements of an iterable (e.g., list of strings) into a single string, with the string itself as separator.
words_to_join = ["Python", "is", "awesome"]
sentence = " ".join(words_to_join)
print(f"Joined sentence: {sentence}")
csv_line = ",".join(fruits_list)
print(f"Joined CSV line: {csv_line}")

# find(substring, start=0, end=len(string)): Returns the lowest index of substring if found, else -1.
# index(substring, start=0, end=len(string)): Same as find(), but raises ValueError if not found.
print(f"Find 'is': {message.find('is')}")     # Output: 7
print(f"Find 'Java': {message.find('Java')}") # Output: -1
# print(message.index('Java')) # Raises ValueError

# replace(old, new, count=-1): Returns a new string with occurrences of 'old' replaced by 'new'.
# 'count' limits the number of replacements.
new_message = message.replace("fun", "powerful")
print(f"Replaced message: {new_message}")

# startswith(prefix, start=0, end=len(string)): True if string starts with prefix.
# endswith(suffix, start=0, end=len(string)): True if string ends with suffix.
print(f"Message starts with 'Python'? {message.startswith('Python')}") # True
print(f"Message ends with 'fun!'? {message.endswith('fun!')}")       # True

# lower(), upper(), capitalize(), title(), swapcase(): Case conversion methods.
print(f"Lowercase: {message.lower()}")
print(f"Uppercase: {message.upper()}")
print(f"Capitalized: {'hello world'.capitalize()}") # Output: Hello world
print(f"Titlecased: {'hello world'.title()}")     # Output: Hello World
print(f"Swapcased: {'HeLlO'.swapcase()}")         # Output: hElLo

# isalpha(), isdigit(), isalnum(), isspace(), islower(), isupper(), istitle(): Check character types.
print(f"'Python'.isalpha()? {'Python'.isalpha()}") # True
print(f"'123'.isdigit()? {'123'.isdigit()}")       # True
print(f"'Py123'.isalnum()? {'Py123'.isalnum()}")   # True (alpha-numeric)
print(f"'   '.isspace()? {'   '.isspace()}")       # True

# format() method and f-strings (Formatted String Literals)
# (f-strings are generally preferred for their conciseness and readability)
name_fmt = "Alice"
age_fmt = 30
# Using format()
formatted_str_method = "My name is {} and I am {} years old.".format(name_fmt, age_fmt)
print(f"Formatted (method): {formatted_str_method}")
# Using f-string (Python 3.6+)
formatted_str_fstring = f"My name is {name_fmt} and I am {age_fmt} years old."
print(f"Formatted (f-string): {formatted_str_fstring}")
# F-strings can include expressions:
print(f"Age next year: {age_fmt + 1}")

# Iterating over a String
print("Characters in 'Python':")
for char in "Python":
    print(char)

# Common Interview Questions/Tips for Strings:
# - Immutability is key: All string methods that "change" a string return a new string.
# - String formatting: f-strings vs. `format()` method vs. older `%` operator. F-strings are modern best practice.
# - Common methods like `split()`, `join()`, `strip()`.
# - Slicing behavior.
# - Time complexity of operations (e.g., concatenation can be O(N*M) in a loop if not careful, better to use `join()`).
# - Unicode and character encodings (basic awareness).

print("\\n" + "-"*60 + "\\n") # Separator for final message
print("End of built_in_data_structures.py")
"""
