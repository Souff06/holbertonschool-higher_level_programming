#!/usr/bin/python3
"""
    if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False
