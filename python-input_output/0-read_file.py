#!/usr/bin/python3
"""Module for reading and printing file contents."""

def read_file(filename=""):
    """Reads a UTF-8 text file and prints its contents to stdout.

    Args:
        filename (str): The path to the file to be read. Defaults to empty string.
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
