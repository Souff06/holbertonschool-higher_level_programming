#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4  # Importer le module compilé

    # Utiliser dir() pour obtenir tous les noms définis dans le module
    names = dir(hidden_4)

    # Filtrer et trier les noms
    for name in sorted(names):
        if not name.startswith("__"):  # Exclure les noms commençant par __
            print(name)  # Afficher les noms un par un
