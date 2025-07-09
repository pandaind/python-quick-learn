"""
# Object-Oriented Programming (OOP)

# OOP is a programming paradigm based on the concept of objects.
# It focuses on creating reusable patterns of code (classes) to produce instances (objects).

# Core Pillars of OOP:
# 1. Encapsulation: Bundling data (attributes) and methods that operate on the data within a single unit (class).
#    It also involves restricting access to some of an object's components (information hiding).
# 2. Abstraction: Hiding complex implementation details and showing only the essential features of the object.
# 3. Inheritance: Creating new classes (derived/child classes) from existing classes (base/parent classes),
#    allowing an "is-a" relationship and code reuse.
# 4. Polymorphism: Allowing objects of different classes to respond to the same method call in different ways
#    (literally "many forms").

print("--- 1. Classes and Objects ---")
# Classes are blueprints for creating objects. Objects are instances of classes.
class Person:
    # Class Attribute (shared among all instances of the class)
    species = "Homo sapiens"

    def __init__(self, name: str, age: int):
        """
        The constructor method, called when an object is created.
        Initializes instance attributes.
        `self` refers to the instance being created.
        """
        # Instance Attributes (specific to each instance)
        self.name = name
        self.age = age

    def greet(self) -> str:
        """An instance method that operates on the instance's data."""
        return f"Hello, my name is {self.name}, I am {self.age} years old. Species: {self.species}."

# Creating objects (instances) of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1.greet())
print(person2.greet())

# Accessing attributes
print(f"{person1.name}'s species: {person1.species}") # Accessing class attribute via instance
print(f"Person class species: {Person.species}")   # Accessing class attribute via class

# Modifying class attribute (affects all instances that haven't overridden it)
Person.species = "Homo sapiens sapiens"
print(f"Updated species for {person1.name}: {person1.greet()}")

# Instance can override class attribute for itself only
person2.species = "Neanderthal" # This creates an instance attribute `species` for person2
print(f"{person2.name}'s species: {person2.species}") # person2 has its own species
print(f"{person1.name}'s species after person2 change: {person1.species}") # person1 still uses class attribute

print("\\n" + "-"*60 + "\\n")
print("--- 2. Inheritance ---")
# Inheritance allows us to define a class that inherits all the methods and properties
# from another class (parent class).

class Student(Person): # Student inherits from Person
    def __init__(self, name: str, age: int, student_id: str, major: str = "Undeclared"):
        """Constructor for Student."""
        super().__init__(name, age) # Call the parent class's __init__ method
        self.student_id = student_id # New instance attribute for Student
        self.major = major           # Another Student-specific attribute

    def study(self) -> str:
        """A method specific to Student."""
        return f"{self.name} (ID: {self.student_id}) is studying {self.major}."

    # Overriding a method from the parent class
    def greet(self) -> str:
        """Overrides the Person's greet method."""
        # return f"Hi, I'm student {self.name}, {self.age}yo, ID: {self.student_id}. Majoring in {self.major}."
        # It's often good practice to call the superclass method if you want to extend functionality
        person_greeting = super().greet()
        return f"{person_greeting} My student ID is {self.student_id} and I major in {self.major}."


student1 = Student("Charlie", 20, "S12345", "Computer Science")
print(student1.greet())
print(student1.study())
print(f"Is student1 an instance of Student? {isinstance(student1, Student)}") # True
print(f"Is student1 an instance of Person? {isinstance(student1, Person)}")   # True (due to inheritance)

# Method Resolution Order (MRO)
# Defines the order in which base classes are searched when looking for a method.
# You can view it using `ClassName.mro()` or `ClassName.__mro__`.
print(f"MRO for Student: {Student.mro()}")

print("\\n" + "-"*60 + "\\n")
print("--- 3. Polymorphism ---")
# Polymorphism means "many forms". In OOP, it refers to the ability of different objects
# to respond to the same method call in their own specific way.

class Animal: # Base class
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str: # Abstract-like method
        raise NotImplementedError("Subclass must implement abstract method `speak`")

class Dog(Animal): # Derived class
    def speak(self) -> str:
        return f"{self.name} says Woof!"

class Cat(Animal): # Derived class
    def speak(self) -> str:
        return f"{self.name} says Meow!"

class Duck(Animal): # Another derived class
    def speak(self) -> str:
        return f"{self.name} says Quack!"

# This function demonstrates polymorphism. It can work with any Animal subclass.
def animal_communication(animals_to_speak: list[Animal]):
    """Takes a list of Animal objects and makes them speak."""
    for animal_obj in animals_to_speak:
        print(animal_obj.speak()) # Calls the appropriate speak() method for each object

dog_instance = Dog("Buddy")
cat_instance = Cat("Whiskers")
duck_instance = Duck("Daffy")

all_animals = [dog_instance, cat_instance, duck_instance]
animal_communication(all_animals)

print("\\n" + "-"*60 + "\\n")
print("--- 4. Encapsulation ---")
# Encapsulation is about bundling data (attributes) and methods that work on that
# data within one unit (class). It also involves restricting access to an object's
# components, which is known as information hiding.

# In Python, there isn't true "private" like in Java/C++.
# Conventions are used:
# - Underscore prefix (`_variable`): A hint to programmers that a variable or method
#   is intended for internal use (often called "protected" by convention).
# - Double underscore prefix (`__variable`): Triggers name mangling (Python renames it
#   to `_ClassName__variable`). This makes it harder to access from outside but isn't true privacy.

class BankAccount:
    def __init__(self, initial_balance: float, account_holder: str):
        self._account_holder = account_holder # "Protected" attribute
        if initial_balance >= 0:
            self.__balance = initial_balance  # "Private-like" attribute (name mangled)
        else:
            self.__balance = 0.0
            print("Initial balance cannot be negative. Set to 0.")

    def deposit(self, amount: float):
        """Deposits a positive amount into the account."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: float):
        """Withdraws an amount if sufficient funds exist."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self) -> float:
        """Provides controlled read-only access to the balance."""
        return self.__balance

    def get_account_holder(self) -> str:
        """Getter for the account holder's name."""
        return self._account_holder

    def set_account_holder(self, name: str):
        """Setter for the account holder's name with basic validation."""
        if name and isinstance(name, str):
            self._account_holder = name
        else:
            print("Invalid account holder name.")

account1 = BankAccount(100.00, "Alice Wonderland")
print(f"Account Holder: {account1.get_account_holder()}, Balance: ${account1.get_balance():.2f}")
account1.deposit(50.50)
account1.withdraw(30.00)
account1.set_account_holder("Alice Kingsleigh")

# Trying to access mangled attribute directly (for demonstration, not good practice)
# print(account1.__balance) # AttributeError: 'BankAccount' object has no attribute '__balance'
print(f"Accessing mangled balance (don't do this!): {account1._BankAccount__balance:.2f}")

print("\\n" + "-"*60 + "\\n")
print("--- 5. Abstraction ---")
# Abstraction means hiding the complex implementation details and showing only the
# essential features (interface) of an object.
# Python's `abc` module (Abstract Base Classes) is used to define abstract classes
# and methods, which enforce that subclasses implement certain methods.

from abc import ABC, abstractmethod

class Shape(ABC): # Inherit from ABC to make it an abstract class
    def __init__(self, shape_name: str):
        self.shape_name = shape_name

    @abstractmethod # Decorator to declare an abstract method
    def area(self) -> float:
        """Abstract method: Subclasses must implement this to calculate area."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Abstract method: Subclasses must implement this to calculate perimeter."""
        pass

    def describe(self) -> str:
        """A concrete method that can be used by all subclasses."""
        return f"This is a shape named {self.shape_name}."

# You cannot create an instance of an abstract class with unimplemented abstract methods:
# try:
#     shape_obj = Shape("Generic") # Raises TypeError
# except TypeError as e:
#     print(f"Error instantiating Shape: {e}")

class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__("Circle") # Call parent's __init__
        self.radius = radius

    def area(self) -> float: # Must implement 'area'
        return 3.14159 * self.radius ** 2

    def perimeter(self) -> float: # Must implement 'perimeter'
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

circle_instance = Circle(5)
rectangle_instance = Rectangle(4, 6)

print(circle_instance.describe())
print(f"Circle Area: {circle_instance.area():.2f}, Perimeter: {circle_instance.perimeter():.2f}")

print(rectangle_instance.describe())
print(f"Rectangle Area: {rectangle_instance.area():.2f}, Perimeter: {rectangle_instance.perimeter():.2f}")

# Polymorphism with abstract base classes
shapes_list: list[Shape] = [circle_instance, rectangle_instance]
print("\\nProcessing shapes polymorphically:")
for shape_item in shapes_list:
    print(f"{shape_item.shape_name} - Area: {shape_item.area():.2f}, Perimeter: {shape_item.perimeter():.2f}")


# Interview Tip:
# - Pillars of OOP: Be ready to explain Encapsulation, Abstraction, Inheritance, and Polymorphism with examples.
# - Name Mangling: Understand how `__` prefix works for "private-like" attributes.
# - Abstract Base Classes (`abc` module): Their role in defining interfaces and ensuring subclasses implement required methods.

# Common Interview Question:
# Q: What is the difference between `@staticmethod` and `@classmethod` in Python?
# A:
#    - `@classmethod`: Takes `cls` (the class itself) as the first implicit argument.
#      It can access and modify class state (class variables). It's often used for factory methods
#      that create instances of the class in a specific way, or to manage class-level configurations.
#    - `@staticmethod`: Does not take any implicit first argument (`self` or `cls`).
#      It's essentially a regular function namespaced within the class. It cannot directly access
#      or modify class state or instance state. It's used for utility functions that are
#      logically related to the class but don't depend on its state.
#
# Q: Explain the MRO (Method Resolution Order).
# A: MRO defines the order in which Python searches for a method in a class hierarchy, especially
#    in cases of multiple inheritance. It uses an algorithm called C3 linearization to ensure a
#    consistent and predictable order. You can inspect the MRO of a class using
#    `ClassName.mro()` or `ClassName.__mro__`. (Example in Inheritance section)
#
# Q: What are Python properties? Why use them?
# A: Properties allow you to define methods (getter, setter, deleter) for an attribute but access
#    it like a simple attribute. This is useful for:
#    1. Data Validation: Ensuring an attribute is set to valid values.
#    2. Computed Attributes: Creating attributes whose values are derived from other data.
#    3. Controlled Access: Exposing a public attribute while keeping the internal storage private-like,
#       allowing you to change the internal implementation without changing the class's public API.
#
# Q: What is the purpose of `__str__` and `__repr__` methods?
# A:
#    - `__str__`: Called by `str()` and `print()`. Should return a user-friendly, readable string
#      representation of the object.
#    - `__repr__`: Called by `repr()`. Should return an unambiguous, official string representation,
#      ideally one that could be used to recreate the object (e.g., `eval(repr(obj))`). If `__str__`
#      is not implemented, `__repr__` is used as a fallback by `str()` and `print()`.
#      It's good practice to always implement `__repr__`.

"""