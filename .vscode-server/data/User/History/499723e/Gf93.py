#!/usr/bin/python3
"""this file contain the class student"""


class Student:
    """class of student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return the choosen attributes or all"""
        if attrs is None:
            return self.__dict__
        attributes_asked = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                attributes_asked[key] = value
        return attributes_asked
