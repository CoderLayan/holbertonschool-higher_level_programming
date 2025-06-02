#!/usr/bin/python3
"""Defines a Student class with filtered JSON serialization"""


class Student:
    """Defines a student by first_name, last_name, and age"""

    def __init__(self, first_name, last_name, age):
        """Initializes the student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance
        If attrs is a list of strings, only includes those attributes
        """
        if (isinstance(attrs, list) and \
                all(isinstance(attr, str) for attr in attrs):
            return {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)
            }
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
