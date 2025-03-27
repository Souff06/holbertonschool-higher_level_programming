#!/usr/bin/python3

def read_file(filename=""):
    with open('mon_fichier.txt', 'r') as fichier:
    contenu = fichier.read()
    print(contenu)