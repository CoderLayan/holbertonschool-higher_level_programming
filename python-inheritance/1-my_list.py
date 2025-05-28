#!/usr/bin/python3
"""Module containing MyList class that inherits from list."""

class MyList(list):
    """A custom list class that inherits from Python's built-in list."""

    def print_sorted(self):
        """Print the list in ascending sorted order.
        
        This method does not modify the original list.
        All elements are assumed to be integers as per requirements.
        """
        sorted_list = sorted(self)
        print(sorted_list)
