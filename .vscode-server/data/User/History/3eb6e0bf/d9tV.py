#!/usr/bin/python3
"""
    create an empty class
"""


class BaseGeometry:
    """
        Public instance method
    """
    def integer_validator(self, name, value):
        isinstance(name, str),
        if isinstance(value, int):
            raise TypeError("must be an integer")
        if value <= 0:
            raise TypeError("must be greater than 0")
