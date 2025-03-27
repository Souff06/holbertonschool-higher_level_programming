#!/usr/bin/python3
"""
    returns True if the object is exactly an instance of the specified
    class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """check the obj prend en compte lhéritage"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
