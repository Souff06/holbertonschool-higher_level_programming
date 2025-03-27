#!/usr/bin/python3
"""
    
"""


def is_same_class(obj, a_class):
    """check the class are inherits or not"""
    if a_class == type(obj):
        return True
    else:
        return False
