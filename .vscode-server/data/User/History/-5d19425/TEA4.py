#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, 'r') as fichier:
        contenu = fichier.read()
        print(contenu)
