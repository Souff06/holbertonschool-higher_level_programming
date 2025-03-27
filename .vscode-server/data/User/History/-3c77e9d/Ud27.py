#!/usr/bin/python3
def add_integer(a, b=98):
    """
        add_integer addition en a et b.
    """
    if not isinstance(a, float):
        raise TypeError("a must be an integer")
    if a < 0:
        raise ValueError("size must be >= 0")
