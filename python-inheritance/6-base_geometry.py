#!/usr/bin/python3
"""
Module 6-base_geometry
Defines a BaseGeometry class with an unimplemented area method.
"""


class BaseGeometry:
    """Represents base geometry with an area method."""

    def area(self):
        """Raises an exception indicating the method is not implemented.

        Raises:
            Exception: area() is not implemented.
        """
        raise Exception("area() is not implemented")
