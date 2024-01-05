import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = self.initialiser_paquet()
        self.main_joueur = []
        self.main_croupier = []

    def initialiser_paquet(self):
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(paquet)
        return paquet

    def calculer_points(self, main):
        points = 0
        as_count = 0

        for carte in main:
            if carte.valeur in ['Valet', 'Dame', 'Roi']:
                points += 10
            elif carte.valeur == 'As':
                as_count += 1
            else:
                points += int(carte.valeur)

        for _ in range(as_count):
            if points + 11 <= 21:
                points += 11
            else:
                points += 1

        return points

    def distribuer_cartes(self):
        self.main_joueur = [self.paquet.pop(), self.paquet.pop()]
        self.main_croupier = [self.paquet.pop(), self.paquet.pop()]

    def afficher_main(self, joueur):
        if joueur == 'joueur':
            main = self.main_joueur
        else:
            main = self.main_croupier

        print(f"Main du {joueur}:")
        for carte in main:
            print(f"{carte.valeur} de {carte.couleur}")

    def jouer(self):
        self.distribuer_cartes()
        self.afficher_main('joueur')
        self.afficher_main('croupier')

        while True:
            action = input("Voulez-vous prendre une carte ? (Oui/Non): ").lower()
            if action == 'oui':
                nouvelle_carte = self.paquet.pop()
                self.main_joueur.append(nouvelle_carte)
                self.afficher_main('joueur')

                if self.calculer_points(self.main_joueur) > 21:
                    print("Vous avez dépassé 21 points. Vous avez perdu!")
                    return
            else:
                break

        while self.calculer_points(self.main_croupier) < 17:
            nouvelle_carte_croupier = self.paquet.pop()
            self.main_croupier.append(nouvelle_carte_croupier)

        self.afficher_main('croupier')

        points_joueur = self.calculer_points(self.main_joueur)
        points_croupier = self.calculer_points(self.main_croupier)

        if points_joueur > 21:
            print("Vous avez dépassé 21 points. Vous avez perdu!")
        elif points_croupier > 21:
            print("Le croupier a dépassé 21 points. Vous avez gagné!")
        elif points_joueur > points_croupier:
            print("Vous avez plus de points que le croupier. Vous avez gagné!")
        elif points_croupier > points_joueur:
            print("Le croupier a plus de points que vous. Vous avez perdu!")
        else:
            print("Égalité!")

jeu_blackjack = Jeu()
jeu_blackjack.jouer()
