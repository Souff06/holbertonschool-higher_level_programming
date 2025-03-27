#!/usr/bin/python3
"""
    Define a class BaseGeometry
"""

class BaseGeometry:
    """
        BaseGeometry class with methods area() and integer_validator()
    """
    def area(self):
        """Raises an Exception because it's not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer"""
        if not isinstance(value, int):  # Vérifie que value est un entier
            raise TypeError(f"{name} must be an integer")
        if value <= 0:  # Vérifie que value est strictement positif
            raise ValueError(f"{name} must be greater than 0")
