"""
# Iterators and Generators

# Iterators are objects that can be iterated upon. Generators are a simple way to create iterators using functions.

# Creating an Iterator
class MyIterator:
    def __init__(self, max):
        self.max = max
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration

my_iter = MyIterator(5)
for num in my_iter:
    print(num)

# Creating a Generator
def my_generator(max):
    current = 0
    while current < max:
        current += 1
        yield current

for num in my_generator(5):
    print(num)

# Interview Tip:
# Be prepared to explain the difference between iterators and generators.

# Common Interview Question:
# How can you create a generator function in Python?
# Use the `yield` keyword inside a function to create a generator.
"""