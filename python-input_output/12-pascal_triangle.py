#!/usr/bin/python3
"""print a pascal triangle"""


def pascal_triangle(n):
    """print a pascal triangle"""
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        current = []
        for j in range(-1, i):
            if j < 0:
                index1 = 0
            else:
                index1 = triangle[i - 1][j]
            if j >= i - 1:
                index2 = 0
            else:
                index2 = triangle[i - 1][j + 1]
            current.append(index1 + index2)
        triangle.append(current)
    return triangle
