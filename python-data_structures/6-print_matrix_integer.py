#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Parcourir chaque ligne de la matrice
    for row in matrix:
        print(" ".join("{:d}".format(elem) for elem in row))
