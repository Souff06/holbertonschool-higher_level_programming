
def print_matrix_integer(matrix=[[]]):
    # Parcourir chaque ligne de la matrice
    for row in matrix:
        # Afficher chaque élément de la ligne avec format, en séparant les éléments par un espace
        print(" ".join("{:d}".format(elem) for elem in row))
