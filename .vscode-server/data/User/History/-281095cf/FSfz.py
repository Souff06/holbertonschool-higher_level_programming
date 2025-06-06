#!/usr/bin/python3
"""
    if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False
"""


def inherits_from(obj, a_class):
    """inherits from class"""
    if isinstance(obj, a_class):
        return True
    elif type(obj) != a_class:
        return True
    else:
        return False
