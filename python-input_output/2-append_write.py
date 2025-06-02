#!/usr/bin/python3
"""Module for appending text to files."""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8) and returns character count.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        chars_added = f.write(text)
    return chars_added
