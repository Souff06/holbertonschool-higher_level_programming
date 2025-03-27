#!/usr/bin/python3

#classe mere
class Vehicule:
    def __init__(self, nom_vehicule, quantite_de_chevaux):
        self.nom = nom_vehicule
        self.chevaux = quantite_de_chevaux

    def se_deplacer(self):
        print("le vehicule {} se deplace ...".format(self.nom))

#classe fille 
class Voiture(Vehicule):
    def __init__(self, nom_voiture, quantite_de_chevaux, portes):
        Vehicule.__init__(self, nom_voiture, quantite_de_chevaux)
        self.portes = portes

v2 = Voiture("m5 will sedan", "1200 ch", 5)
Voiture2.se_deplacer()