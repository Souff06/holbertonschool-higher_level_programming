#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    length = len(roman_string)

    for i in range(length):
        # Vérification que le caractère est valide
        if roman_string[i] not in roman_dict:
            return 0  # Ou lancer une exception

        # Si la valeur actuelle est inférieure à la suivante, on la soustrait
        if (i < length - 1 and 
                roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]):
            total -= roman_dict[roman_string[i]]
        else:
            # Sinon, on l'ajoute
            total += roman_dict[roman_string[i]]

    return total
