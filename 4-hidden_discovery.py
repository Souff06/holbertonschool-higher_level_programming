#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # Récupérer tous les noms définis dans le module
    names = dir(hidden_4)

    # Filtrer et trier les noms qui ne commencent pas par "__"
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)

