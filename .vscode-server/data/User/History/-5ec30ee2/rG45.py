
# Importer la classe Rectangle du fichier 9-rectangle
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    def __init__(self, size):
        # Valider la taille avec la méthode integer_validator
        self.integer_validator("size", size)
        # Appeler le constructeur de la classe parente Rectangle
        super().__init__(size, size)
        # Attribut privé size
        self.__size = size

    def area(self):
        # Calculer l'aire du carré (taille * taille)
        return self.__size * self.__size

    def __str__(self):
        # Retourner la représentation sous forme [Rectangle] size/size
        return f"[Rectangle] {self.__size}/{self.__size}"
