#!/usr/bin/python3
"""Defines a MyList class that inherits from list."""

class MyList(list):
    """A subclass of list with additional print_sorted method."""

    def print_sorted(self):
        """Print the list in ascending sorted order.
        
        Works with empty lists and preserves the original list.
        """
        print(sorted(self.copy()))
