#!/usr/bin/python3
# Mixin pour nager
class SwimMixin:
    def swim(self):
        print("The creature swims!")

# Mixin pour voler
class FlyMixin:
    def fly(self):
        print("The creature flies!")

# Classe principale Dragon qui hérite des mixins
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
