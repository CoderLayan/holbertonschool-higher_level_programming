#!/usr/bin/python3
"""Defines a square with private size attribute."""

class Square:
    """Class that defines a square with private size attribute."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
