#!/usr/bin/python3
"""Module for converting JSON strings to Python objects."""

import json


def from_json_string(my_str):
    """Returns a Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert to a Python object.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
