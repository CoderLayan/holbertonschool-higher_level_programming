#!/usr/bin/python3
"""Defines a Square class with private size attribute."""

class Square:
    """Represents a square with private size attribute.

    This class demonstrates encapsulation by making the size attribute private,
    which prevents direct modification from outside the class. Future tasks will
    add methods to safely access and modify this attribute.

    Attributes:
        __size (int): The size of the square (private)
    """
    
    def __init__(self, size):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the new square.
                       Currently no type or value verification is performed.
        """
        self.__size = size
