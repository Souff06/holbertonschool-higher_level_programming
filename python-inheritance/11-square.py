#!/usr/bin/python3
"""
    Module containing BaseGeometry, Rectangle, and Square classes.
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
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
        Rectangle class that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
        Square class that inherits from Rectangle
    """

    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)  # Validate size
        self.__size = size
        super().__init__(size, size)  # Call Rectangle constructor

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Returns a string representation of the square"""
        return f"[Square] {self.__size}/{self.__size}"
