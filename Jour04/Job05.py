class Forme:
    def aire(self):
        return 0


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur
import math

class Forme:
    def aire(self):
        return 0


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur


class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon**2

rectangle = Rectangle(largeur=5, hauteur=3)
resultat_aire_rectangle = rectangle.aire()
print(f"Aire du rectangle : {resultat_aire_rectangle}")

cercle = Cercle(rayon=4)
resultat_aire_cercle = cercle.aire()
print(f"Aire du cercle : {resultat_aire_cercle}")

rectangle = Rectangle(largeur=5, hauteur=3)
resultat_aire = rectangle.aire()
print(f"Aire du rectangle : {resultat_aire}")
