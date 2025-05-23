#!/usr/bin/python3
"""Defines a Square class with private size attribute."""


class Square:
    """Represents a square with private instance attribute size.
    
    Attributes:
        __size (int): Size of the square (private)
    """
    
    def __init__(self, size):
        """Initializes a new Square instance.
        
        Args:
            size (int): The size of the new square.
        """
        self.__size = size
