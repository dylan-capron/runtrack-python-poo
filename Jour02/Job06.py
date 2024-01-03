class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}  
        self.__statut_commande = "En cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        if nom_plat not in self.__plats_commandes:
            self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": "En cours"}
            print(f"Plat ajouté à la commande : {nom_plat}")

    def annuler_commande(self):
        self.__plats_commandes = {}
        self.__statut_commande = "Annulée"
        print("Commande annulée.")

    def __calculer_total(self):
        total = sum(plat["prix"] for plat in self.__plats_commandes.values())
        return total

    def afficher_commande(self):
        print(f"Commande n°{self.__numero_commande} - Statut : {self.__statut_commande}")
        for nom_plat, details_plat in self.__plats_commandes.items():
            print(f"{nom_plat} - Prix : {details_plat['prix']}€ - Statut : {details_plat['statut']}")
        total = self.__calculer_total()
        print(f"Total à payer : {total}€ (TVA incluse)")

    def calculer_tva(self, taux_tva):
        total = self.__calculer_total()
        tva = total * taux_tva / 100
        print(f"Montant de la TVA ({taux_tva}%): {tva}€")

ma_commande = Commande(numero_commande=1)

ma_commande.ajouter_plat(nom_plat="Pizza Margherita", prix_plat=10)
ma_commande.ajouter_plat(nom_plat="Salade César", prix_plat=8)
ma_commande.ajouter_plat(nom_plat="Pâtes Carbonara", prix_plat=12)

ma_commande.afficher_commande()

ma_commande.calculer_tva(taux_tva=10)

ma_commande.annuler_commande()

ma_commande.afficher_commande()
