#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcule la factorielle d'un nombre entier non négatif.

    La fonction utilise une approche récursive pour calculer la 
    factorielle d'un nombre. La factorielle de n (notée n!) est le 
    produit de tous les entiers positifs inférieurs ou égaux à n.

    Parameters:
    n (int): Un entier non négatif dont la factorielle est à calculer.

    Returns:
    int: La valeur de la factorielle de n. Pour n = 0, retourne 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
