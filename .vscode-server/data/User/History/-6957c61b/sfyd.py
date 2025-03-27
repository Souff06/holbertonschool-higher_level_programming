#!/usr/bin/python3
for i in range(100):
    if i == 99:  # Si c'est le dernier élément, pas de virgule
        print(f"{i:02d}")
    else:
        print(f"{i:02d}, ", end="")
