#!/usr/bin/python3
def add_integer(a, b=98):
    """
        add_integer addition en a et b.
    """
    
    if not type(a) in [int, float]:
        raise TypeError("a must be an integer")
    if not type(b) in [int, float]:
        raise TypeError("b must be an integer")
    if type (a) is float:
        a = int(a)
    if type (b) is float:
        b = int(b)    
    return (a + b)
