#!/usr/bin/python3

#classe mere
class Vehicule:
    def __init__(self, nom, quantite_essence):
        self.nom = nom
        self.essence = quantite_essence

#classe fille 
#class Voiture(Vehicule):

v1 = Vehicule("F22", 1400)
print(v1.nom)
