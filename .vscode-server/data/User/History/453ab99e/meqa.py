#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a number using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated

    Returns:
    int: The factorial of the integer n
    """
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    f = factorial(int(sys.argv[1]))
    print(f)
