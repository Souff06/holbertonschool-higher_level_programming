#!/usr/bin/env python3

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convertit un fichier CSV en un fichier JSON.

    :param csv_filename: Le nom du fichier CSV à convertir.
    :return: True si la conversion a réussi, False sinon.
    """
    try:
        # Liste pour stocker les lignes du fichier CSV
        data = []

        # Ouverture du fichier CSV
        with open(csv_filename, mode='r') as csv_file:
            # Utilisation de DictReader pour lire les données
            # en tant que dictionnaire
            csv_reader = csv.DictReader(csv_file)

            # Ajouter chaque ligne du CSV comme dictionnaire à la liste
            for row in csv_reader:
                data.append(row)

        # Sérialisation des données en JSON et écriture dans data.json
        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        print(f"Data from {csv_filename} has been converted to data.json")
        return True
    except FileNotFoundError:
        print(f"File {csv_filename} not found.")
        return False
    except Exception as e:
        print(f"An error occurred during conversion: {e}")
        return False
