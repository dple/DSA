"""
Counter is a sub-class that is used to count hashable objects. It implicitly creates a hash table of an iterable when invoked.
"""
from collections import Counter

# Counter from a string
c = Counter("GeeksforGeeks")

print(c)
for e in c.elements():
    print(e, end = ' ')
print()

# Counter from a list/array
arr = [12, 3, 4, 3, 5, 11, 12, 6, 7]

c = Counter(arr)
print(c)
for e in c.elements():
    print(e, end = ' ')
print()

# List the elements and their occurrences
for key, value in zip(c.keys(), c.values()):
    print(key, value)