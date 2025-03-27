#!/usr/bin/env python3

import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Affiche les attributs de l'objet dans le format demandé.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Sérialise l'objet courant dans un fichier spécifié en utilisant le module pickle.
        
        :param filename: Nom du fichier où enregistrer l'objet sérialisé.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            print(f"Object serialized and saved to '{filename}'.")
        except Exception as e:
            print(f"Error occurred during serialization: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Désérialise un objet à partir d'un fichier en utilisant le module pickle.
        
        :param filename: Nom du fichier où l'objet sérialisé est sauvegardé.
        :return: Une instance de CustomObject ou None en cas d'erreur.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            return obj
        except Exception as e:
            print(f"Error occurred during deserialization: {e}")
            return None
