class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1

    def position(self):
        return (self.x, self.y)

personnage = Personnage(x=2, y=3)

# Affichage de la position initiale
print("Position initiale :", personnage.position())

personnage.droite()

print("Nouvelle position :", personnage.position())

personnage.bas()

print("Position après déplacement vers le bas :", personnage.position())
