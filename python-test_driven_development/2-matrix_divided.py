#!/usr/bin/python3
"""
    divides all elements of a matrix
    two arguments: matrix and div
    return: new matrix
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div, rounded to 2 decimal places."""
    
    # Vérification que `matrix` est une liste de listes d'entiers ou de flottants
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Vérification que tous les éléments de `matrix` sont des nombres
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Vérification que toutes les lignes ont la même taille
    row_length = len(matrix[0])  # On récupère la taille de la première ligne
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Vérification que `div` est un nombre (int ou float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Vérification que `div` n'est pas égal à zéro
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Création d'une nouvelle matrice avec les valeurs divisées et arrondies à 2 décimales
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    
    return new_matrix
