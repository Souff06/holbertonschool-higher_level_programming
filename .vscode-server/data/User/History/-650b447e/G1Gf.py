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
    
class Moto(Vehicule):
    def __init__(self, nom_vehicule, quantite_de_chevaux, pot):
        Vehicule.__init__(self, nom_vehicule, quantite_de_chevaux)
        self.pot = pot

v1 = Moto("Tracer 700", "75 ch", "Arrow")
v2 = Voiture("m5 will sedan", "1200 ch", 5)
v1.se_deplacer()
v2.se_deplacer()

print(v2.chevaux)