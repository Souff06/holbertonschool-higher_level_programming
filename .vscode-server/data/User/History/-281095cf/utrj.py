#!/usr/bin/python3
"""
    if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False
"""


def is_same_class(obj, a_class):
    return type(obj) is a_class
