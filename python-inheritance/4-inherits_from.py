#!/usr/bin/python3
"""
    if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False
"""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a subclass of a_class"""
    return isinstance(obj, a_class) and type(obj) != a_class

