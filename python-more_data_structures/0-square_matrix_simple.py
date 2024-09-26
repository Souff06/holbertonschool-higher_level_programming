#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for number in matrix:
        new_list = []
        for index in number:
            new_list.append(index ** 2)
        new_matrix.append(new_list)
    return new_matrix
