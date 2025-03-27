#!/usr/bin/python3
for i in range(0, 9):
    # Parcourir le deuxième chiffre, qui commence toujours à un de plus que le premier chiffre
    for j in range(i + 1, 10):
        # Vérifier si c'est la dernière paire à imprimer pour éviter une virgule finale
        if i == 8 and j == 9:
            print(f"{i}{j}")
        else:
            print(f"{i}{j}", end=", ")