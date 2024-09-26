#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    # Initialiser avec le premier élément de la liste
    max_value = my_list[0]

    # Parcourir la liste à partir du deuxième élément
    for num in my_list[1:]:
        if num > max_value:
            max_value = num

    return max_value
