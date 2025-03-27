
from abc import ABC, abstractmethod

# Classe abstraite Animal
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# Sous-classe Dog qui hérite d'Animal
class Dog(Animal):
    def sound(self):
        return "Bark"

# Sous-classe Cat qui hérite d'Animal
class Cat(Animal):
    def sound(self):
        return "Meow"
