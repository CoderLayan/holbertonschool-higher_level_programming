#!/usr/bin/python3
"""Defines a MyList class that inherits from list with sorting capability."""

class MyList(list):
    """Enhanced list class with sorted printing functionality.

    Inherits all standard list behavior and adds print_sorted() method.
    Handles positive numbers, negative numbers, and empty lists.
    """

    def print_sorted(self):
        """Print the list in ascending sorted order.

        Examples:
            >>> my_list = MyList()
            >>> my_list.append(3)
            >>> my_list.append(-1)
            >>> my_list.append(2)
            >>> my_list.print_sorted()
            [-1, 2, 3]
            >>> print(my_list)
            [3, -1, 2]
            >>> empty = MyList()
            >>> empty.print_sorted()
            []
        """
        print(sorted(self))
