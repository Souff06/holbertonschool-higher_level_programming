#!/usr/bin/python3
"""
    inheritance Mylist form list and print sorted
"""


class MyList(list):
    """fonction inherits from list"""
    def print_sorted(self):
        print(sorted(self))
