#!/usr/bin/python3
"""
    divides all elements of a matrix
    two arguments: matrix and div
    return: new matrix
"""


def matrix_divided(matrix, div):
    """
        divides all elements of a matrix
    """
    result_matrix = []
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    for sublist in matrix:
        for elem in sublist:
            if type(elem) not in [int, float]:
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats")
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(round(num / div, 2))
        result_matrix.append(new_row)
    return result_matrix
