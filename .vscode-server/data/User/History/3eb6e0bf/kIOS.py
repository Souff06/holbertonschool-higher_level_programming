#!/usr/bin/python3
"""
    Module containing the BaseGeometry class
"""

class BaseGeometry:
    """
        BaseGeometry class with methods area() and integer_validator()
    """
    def area(self):
        """Raises an Exception because area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer
        :param name: always a string
        :param value: value to validate
        :raises TypeError: if value is not an integer
        :raises ValueError: if value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

