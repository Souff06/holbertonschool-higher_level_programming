#!/usr/bin/env python3


import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialise un dictionnaire Python et l'enregistre dans un fichier JSON.

    :param data: Dictionnaire Python à sérialiser.
    :param filename: Nom du fichier de sortie (JSON).
    """
    try:
        # Ouverture du fichier en mode écriture
        with open(filename, 'w') as file:
            # Sérialisation des données en JSON et écriture dans le fichier
            json.dump(data, file)
        print(f"Data serialized and saved to '{filename}'.")
    except Exception as e:
        print(f"Error occurred during serialization: {e}")


def load_and_deserialize(filename):
    """
    Charge un fichier JSON et désérialise son 
    contenu pour recréer un dictionnaire Python.

    :param filename: Nom du fichier d'entrée (JSON).
    :return: Dictionnaire Python avec les données désérialisées.
    """
    try:
        # Ouverture du fichier en mode lecture
        with open(filename, 'r') as file:
            # Chargement des données du fichier JSON et désérialisation
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error occurred during deserialization: {e}")
        return None
