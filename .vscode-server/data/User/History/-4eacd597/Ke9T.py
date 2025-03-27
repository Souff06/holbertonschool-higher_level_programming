#!/usr/bin/python3
"""Define a Square class."""


class Square:
    """Class Square with a size attribute."""
    def __init__(self, size=0):
        """
            Initialize a new instance of the Square class.
            size (int): The size of the square.
        """
        self.__size = size
        try:
            raise TypeError ('size must be an integer')
        except ValueError:
            print("size must be >= 0")
