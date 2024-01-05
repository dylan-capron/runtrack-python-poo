class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur

    @property
    def longueur(self):
        return self._longueur

    @property
    def largeur(self):
        return self._largeur

    @longueur.setter
    def longueur(self, value):
        self._longueur = value

    @largeur.setter
    def largeur(self, value):
        self._largeur = value

    def perimetre(self):
        return 2 * (self._longueur + self._largeur)

    def surface(self):
        return self._longueur * self._largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self._hauteur = hauteur

    @property
    def hauteur(self):
        return self._hauteur

    @hauteur.setter
    def hauteur(self, value):
        self._hauteur = value

    def volume(self):
        return self._longueur * self._largeur * self._hauteur


rectangle = Rectangle(longueur=5, largeur=3)
print(f"Périmètre du rectangle : {rectangle.perimetre()}")
print(f"Surface du rectangle : {rectangle.surface()}")

parallelepipede = Parallelepipede(longueur=4, largeur=2, hauteur=3)
print(f"Volume du parallélépipède : {parallelepipede.volume()}")
