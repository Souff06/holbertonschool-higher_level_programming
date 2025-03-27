#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Remplace un élément d'une liste à une position spécifique."""
    if idx < 0 or idx >= len(my_list):
        return my_list  # Retourne la liste originale si l'indice est invalide
    my_list[idx] = element  # Remplace l'élément à l'indice donné
    return my_list
