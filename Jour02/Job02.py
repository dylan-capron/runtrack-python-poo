class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages
        self.__disponible = True  # Ajout de l'attribut disponible

    # Accesseurs (getters)
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

    # Méthode pour vérifier la disponibilité du livre
    def vérification(self):
        return self.__disponible

    # Méthode pour emprunter le livre
    def emprunter(self):
        if self.vérification():
            print("Livre emprunté.")
            self.__disponible = False
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

    # Méthode pour rendre le livre
    def rendre(self):
        if not self.vérification():
            print("Livre rendu.")
            self.__disponible = True
        else:
            print("Le livre n'a pas été emprunté. Impossible de le rendre.")

# Exemple d'utilisation de la classe
mon_livre = Livre(titre="Python pour les nuls", auteur="John Doe", nombre_pages=300)

# Vérification de la disponibilité initiale du livre
print("Le livre est disponible :", mon_livre.vérification())

# Emprunt du livre
mon_livre.emprunter()

# Tentative de réemprunt du livre (devrait afficher un message d'indisponibilité)
mon_livre.emprunter()

# Rendre le livre
mon_livre.rendre()

# Tentative de rendre le livre à nouveau (devrait afficher un message de disponibilité)
mon_livre.rendre()
