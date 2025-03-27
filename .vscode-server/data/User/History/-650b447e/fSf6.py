#!/usr/bin/python3

#classe mere
class Vehicule:
    def __init__(self, nom, quantite_essence):
        self.nom = nom
        self.essence = quantite_essence
    
    def montrer_vehicule(self):
        return self.nom
    
class