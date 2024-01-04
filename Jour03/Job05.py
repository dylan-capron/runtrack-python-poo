import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(1, 10)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisir_niveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1, 2, 3) : "))

    def lancer_jeu(self):
        joueur = Personnage("Joueur", 100 * self.niveau)
        ennemi = Personnage("Ennemi", 50 * self.niveau)

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            if ennemi.vie <= 0:
                print(f"{joueur.nom} a vaincu l'ennemi {ennemi.nom}!")
                break

            ennemi.attaquer(joueur)
            if joueur.vie <= 0:
                print(f"{ennemi.nom} a vaincu le joueur {joueur.nom}.")
                break

            print(f"{joueur.nom} : {joueur.vie} points de vie | {ennemi.nom} : {ennemi.vie} points de vie")

jeu = Jeu()
jeu.choisir_niveau()
jeu.lancer_jeu()
