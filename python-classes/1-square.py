#!/usr/bin/python3
"""
Module 1-square
Defines a Square class with a private size attribute.
"""


class Square:
    """Represents a square with a private instance attribute 'size'."""

    def __init__(self, size):
        """Initializes a new square with a given size.
        
        Args:
            size (int): The size of the square.
        """
        self.__size = size
