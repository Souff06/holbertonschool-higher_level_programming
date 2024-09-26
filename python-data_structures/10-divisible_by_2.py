#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Créer une nouvelle liste qui stockera les résultats (True ou False)
    result_list = []
    
    # Parcourir chaque élément de la liste d'origine
    for num in my_list:
        # Vérifier si l'élément est divisible par 2
        if num % 2 == 0:
            result_list.append(True)
        else:
            result_list.append(False)
    
    # Retourner la nouvelle liste
    return result_list
