#!/usr/bin/python3

def square_matrix_simple(matrix=()):
    matrix_sq=[]
    for i in range(len(matrix)):
        matrix[i] = i**2
    return matrix_sq

