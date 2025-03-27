#!/usr/bin/python3

def square_matrix_simple(matrix=()):
    matrix_sq=[]
    for i in range(len(matrix)-1):
        matrix_sq[i] = i**2
    return matrix_sq

  

matrix = [

[1, 2, 3,7,8,9],

[4, 5, 6,7,8,9],

[7, 8, 9,7,8,9],

[7, 8, 9,7,8,9],

]

matrice2=square_matrix_simple(matrix)

print(matrice2)