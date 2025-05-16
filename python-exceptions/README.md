# Python - Exceptions

This project contains Python scripts that demonstrate exception handling.

## Tasks

### 0. Safe list printing
**File:** `0-safe_print_list.py`

A function that prints `x` elements of a list.
- Prototype: `def safe_print_list(my_list=[], x=0):`
- Prints all elements on the same line followed by a new line
- Returns the real number of elements printed
- Handles cases where `x` is bigger than the list length
- Uses `try`/`except` without importing modules or using `len()`

Example usage:
```python
my_list = [1, 2, 3, 4, 5]
nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
