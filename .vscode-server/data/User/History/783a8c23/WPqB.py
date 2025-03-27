#!/usr/bin/python3
for i in range(10):
for j in range(i + 1, 10):
    if i != j:
        if i == 8 and j == 9:  # Dernière combinaison, ne pas mettre de virgule
            print(f"{i:02d}{j:02d}")
        else:
            print(f"{i:02d}{j:02d}", end=", ")
