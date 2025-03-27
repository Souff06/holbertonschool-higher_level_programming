#!/usr/bin/python3
class VerboseList(list):
    # Redéfinir la méthode append pour ajouter une notification
    def append(self, item):
        super().append(item)  # Appeler la méthode append de la classe parente
        print(f"Added [{item}] to the list.")

    # Redéfinir la méthode extend pour ajouter une notification
    def extend(self, items):
        super().extend(items)  # Appeler la méthode extend de la classe parente
        print(f"Extended the list with [{len(items)}] items.")

    # Redéfinir la méthode remove pour ajouter une notification
    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)  # Appeler la méthode remove de la classe parente

    # Redéfinir la méthode pop pour ajouter une notification
    def pop(self, index=-1):
        item = self[index]  # Obtenir l'élément avant de le supprimer
        super().pop(index)  # Appeler la méthode pop de la classe parente
        print(f"Popped [{item}] from the list.")
