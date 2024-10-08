#!/usr/bin/env python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Sérialise un dictionnaire Python en un fichier XML.

    :param dictionary: Le dictionnaire à sérialiser.
    :param filename: Le nom du fichier où sauvegarder l'XML.
    """
    # Créer l'élément racine
    root = ET.Element("data")

    # Ajouter chaque clé-valeur comme sous-élément
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Créer un arbre XML à partir de l'élément racine
    tree = ET.ElementTree(root)

    # Sauvegarder l'arbre XML dans un fichier
    try:
        with open(filename, 'wb') as xml_file:
            tree.write(xml_file)
        print(f"Dictionary serialized to {filename}")
    except Exception as e:
        print(f"Error occurred during XML serialization: {e}")


def deserialize_from_xml(filename):
    """
    Désérialise un fichier XML en un dictionnaire Python.

    :param filename: Le nom du fichier XML à lire.
    :return: Un dictionnaire Python avec les données désérialisées.
    """
    try:
        # Parse le fichier XML
        tree = ET.parse(filename)
        root = tree.getroot()

        # Recréer le dictionnaire à partir des éléments XML
        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text

        return dictionary
    except Exception as e:
        print(f"Error occurred during XML deserialization: {e}")
        return None
