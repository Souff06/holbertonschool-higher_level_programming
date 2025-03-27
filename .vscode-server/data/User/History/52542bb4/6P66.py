#!/usr/bin/python3
"""
    returns the list of available attributes and methods of an object
"""


class MyList(list):
    """fonction inherits from list"""
    def print_sorted(self):
        print(sorted(self))
