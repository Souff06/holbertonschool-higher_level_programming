#!/usr/bin/python3
"""
    create an empty class
"""


class BaseGeometry:
    """
        Public instance method
    """
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if value != 