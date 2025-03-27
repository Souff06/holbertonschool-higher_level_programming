#!/usr/bin/python3
"""
Function to print all integers of a list, one per line.
"""

def print_list_integer(my_list=[]):
    """
    Prints each integer in the list on a new line.
    
    Args:
        my_list: List of integers to be printed.
    """
    for number in my_list:
        # Print each integer using str.format()
        print("{}".format(number))
