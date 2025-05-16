#!/usr/bin/python3
"""
This module provides a function called add_integer
that adds two integers or floats and returns an integer result.
It validates the input types and casts floats to integers.
"""
def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the sum as an integer.
    
    Args:
        a: The first number, can be an integer or a float.
        b: The second number, can be an integer or a float (default is 98).
    
    Returns:
        An integer, the sum of `a` and `b`.
    
    Raises:
        TypeError: If `a` or `b` is not an integer or float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)  # Casting to integer before returning
