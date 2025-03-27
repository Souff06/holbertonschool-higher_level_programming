#!/usr/bin/python3

#classe mere
class Vehicule:
    def __init__(self, nom, quantite_de_chevaux):
        self.nom = nom
        self.chevaux = quantite_de_chevaux

#classe fille 
#class Voiture(Vehicule):

v1 = Vehicule("F22 Raptor", 3500 )
v2 = Vehicule("m5 will sedan", 1200)
print(v1.nom, v1.chevaux)
print(v2.nom, v2.chevaux)