#!/usr/bin/python3
"""
    inher
"""


class MyList(list):
    """fonction inherits from list"""
    def print_sorted(self):
        print(sorted(self))
