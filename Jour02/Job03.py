class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages
        self.__disponible = True  

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_pages(self):
        return self.__nombre_pages

    def get_disponible(self):
        return self.__disponible

    # Mutateurs (setters)
    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def set_auteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur

    def set_nombre_pages(self, nouveau_nombre_pages):
        if isinstance(nouveau_nombre_pages, int) and nouveau_nombre_pages > 0:
            self.__nombre_pages = nouveau_nombre_pages
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")

    def vérification(self):
        return self.__disponible

    def emprunter(self):
        if self.vérification():
            print("Livre emprunté.")
            self.__disponible = False
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

    def rendre(self):
        if not self.vérification():
            print("Livre rendu.")
            self.__disponible = True
        else:
            print("Le livre n'a pas été emprunté. Impossible de le rendre.")

mon_livre = Livre(titre="Python pour les nuls", auteur="John Doe", nombre_pages=300)

print("Le livre est disponible :", mon_livre.vérification())

mon_livre.emprunter()

mon_livre.emprunter()

mon_livre.rendre()

mon_livre.rendre()
