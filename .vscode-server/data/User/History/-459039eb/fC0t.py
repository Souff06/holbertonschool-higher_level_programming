#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_sq=[]

    for i in matrix:
        ligne=[]
        for j in i:
            ligne.append(j**2)
        matrix_sq.append(ligne)
    return matrix_sq
