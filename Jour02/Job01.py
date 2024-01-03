class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur

    def getLongueur(self):
        return self._longueur

    def getLargeur(self):
        return self._largeur

    def setLongueur(self, nouvelle_longueur):
        self._longueur = nouvelle_longueur

    def setLargeur(self, nouvelle_largeur):
        self._largeur = nouvelle_largeur

rectangle1 = Rectangle(longueur=10, largeur=5)

print("Longueur initiale :", rectangle1.getLongueur())
print("Largeur initiale :", rectangle1.getLargeur())

rectangle1.setLongueur(15)
rectangle1.setLargeur(8)

print("Nouvelle longueur :", rectangle1.getLongueur())
print("Nouvelle largeur :", rectangle1.getLargeur())
