#!/usr/bin/python3
"""Module for creating objects from JSON files."""

import json


def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename (str): The JSON file to read from.

    Returns:
        object: The Python data structure loaded from the file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
