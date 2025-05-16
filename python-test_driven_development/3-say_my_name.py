#!/usr/bin/python3
"""Defines a name-printing function."""

def say_my_name(first_name, last_name=""):
    """Print a name in the format 'My name is <first name> <last name>'.

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print. Defaults to "".

    Raises:
        TypeError: If either first_name or last_name are not strings.
        TypeError: If first_name is missing.
    """
    if first_name is None:
        raise TypeError("say_my_name() missing 1 required positional argument: 'first_name'")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
