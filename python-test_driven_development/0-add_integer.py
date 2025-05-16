#!/usr/bin/python3
"""
Module for adding two integers
"""

def add_integer(a, b=98):
    """
Adds two integers or floats and returns an integer sum.

Args:
    a (int, float): First number.
    b (int, float, optional): Second number, defaults to 98.

Raises:
    TypeError: If a or b are not integers or floats.

Returns:
    int: Sum of a and b.
"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
