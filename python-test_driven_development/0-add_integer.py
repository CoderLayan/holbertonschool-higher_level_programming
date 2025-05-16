#!/usr/bin/python3
"""Defines an integer addition function."""

def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Args:
        a (int or float): The first number.
        b (int or float): The second number. Defaults to 98.

    Raises:
        TypeError: If either a or b is a non-integer and non-float.
        ValueError: If either a or b is NaN or infinity.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Check for NaN or infinity
    if isinstance(a, float) and (a != a or abs(a) == float('inf')):
        raise ValueError("cannot convert float NaN to integer")
    if isinstance(b, float) and (b != b or abs(b) == float('inf')):
        raise ValueError("cannot convert float NaN to integer")
    
    # Handle very large floats by converting to int first
    try:
        a_int = int(a)
        b_int = int(b)
    except OverflowError:
        # For very large numbers, we'll let Python handle the conversion
        a_int = int(a)
        b_int = int(b)
    
    return a_int + b_int
