#!/usr/bin/python3

def square_matrix_simple(matrix=()):
    matrix_sq=[]
    for i in range(len(matrix)-1):
        matrix_sq[i] = i**2
    return matrix_sq

  

matrice2=square_matrix_simple(matrix)

print(matrice2)