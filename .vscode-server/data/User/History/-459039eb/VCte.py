#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_sq=[]
    for i in matrix: 
        for j in range(len(i)-1): 
            ligne=[] 
            ligne.append(j**2) 
            matrix_sq.append(ligne)
            
    return matrix_sq


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrice2=square_matrix_simple(matrix)
print(matrice2)

def square_matrix_simple(matrix=[]):
    matrix_sq=[]
    for i in range (matrix)