#!/usr/bin/python3
import sys
sys.path.append('/tmp')  # Ajoute /tmp au chemin de recherche des modules

if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
