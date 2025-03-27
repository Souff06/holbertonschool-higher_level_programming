#!/usr/bin/python3
class CountedIterator:
    def __init__(self, iterable):
        # Initialiser l'itérateur et le compteur
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        # Incrémenter le compteur et récupérer le prochain élément
        try:
            item = next(self.iterator)  # Appeler l'itérateur interne
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration  # Propager l'exception lorsque la séquence est terminée

    def get_count(self):
        # Retourner le nombre d'éléments itérés
        return self.count
