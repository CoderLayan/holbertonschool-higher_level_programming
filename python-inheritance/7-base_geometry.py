#!/usr/bin/python3
"""
Module 7-base_geometry
Defines a BaseGeometry class with an unimplemented area method and integer validation.
"""


class BaseGeometry:
    """Represents base geometry with validation methods."""

    def area(self):
        """Raises an exception indicating the method is not implemented.

        Raises:
            Exception: area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer.

        Args:
            name (str): The name of the variable.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
