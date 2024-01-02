class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"X : {self.x}")

    def afficherY(self):
        print(f"Y : {self.y}")

    def changerX(self, nouvelle_valeur_x):
        self.x = nouvelle_valeur_x

    def changerY(self, nouvelle_valeur_y):
        self.y = nouvelle_valeur_y

point1 = Point(2, 3)

point1.afficherLesPoints()

point1.afficherX()

# Affichage de la coordonnée y
point1.afficherY()

point1.changerX(5)
point1.changerY(7)

point1.afficherLesPoints()
