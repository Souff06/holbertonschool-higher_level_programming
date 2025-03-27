#!/usr/bin/python3

#classe mere
class Vehicule:
    def __init__(self, nom, quantite_de_chevaux):
        self.nom = nom
        self.chevaux = quantite_de_chevaux

    def se_deplacer(self):
        print("le vehicule {} se deplace ...".format(self.nom))

#classe fille 
class Voiture(Vehicule):
    def __init__(self, nom, quantite_de_chevaux, portes):
        Vehicule.__init__(nom, quantite_de_chevaux, portes)
        self.portes = portes

v2 = Vehicule("m5 will sedan", 1200, 5)
print(v2.nom, v2.chevaux)
Voiture2.se_deplacer()