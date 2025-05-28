#!/usr/bin/python3
"""Module containing MyList class that inherits from list."""


class MyList(list):
    """Class that inherits from list with additional print_sorted method."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
