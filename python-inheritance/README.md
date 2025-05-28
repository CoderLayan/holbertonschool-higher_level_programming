# Python - Inheritance

## Task 0: Lookup

Write a function that returns the list of available attributes and methods of an object.

### Requirements:
- Prototype: `def lookup(obj):`
- Returns a list object
- You are not allowed to import any module

### Example Usage:
```python
lookup = __import__('0-lookup').lookup

class MyClass1(object):
    pass

print(lookup(MyClass1))
# Output will show all default Python object attributes/methods
