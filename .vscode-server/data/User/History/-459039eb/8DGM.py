#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_sq=[]
    for i in matrix: # 3 * [1, 2, 3] 
        for j in range(len(i)-1): # 3  1 2 3
            ligne=[] # VIDE
            ligne.append(j**2) # 1 4 9
            matrix_sq.append(ligne)
            
    return matrix_sq


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
square_matrix_simple(matrix)