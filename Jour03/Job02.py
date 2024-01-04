class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde_initial, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde_initial
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Compte n°{self.__numero_compte} - Titulaire : {self.__prenom} {self.__nom}")
        print(f"Solde : {self.__solde}€")

    def afficher_solde(self):
        print(f"Solde du compte n°{self.__numero_compte} : {self.__solde}€")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant}€ effectué. Nouveau solde : {self.__solde}€")

    def retrait(self, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant}€ effectué. Nouveau solde : {self.__solde}€")
        else:
            print("Opération impossible : Solde insuffisant.")

    def agios(self, taux_agios):
        if self.__solde < 0:
            agios = abs(self.__solde) * taux_agios / 100
            self.__solde -= agios
            print(f"Agios appliqués. Nouveau solde : {self.__solde}€")

    def virement(self, compte_destinataire, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant}€ effectué vers le compte n°{compte_destinataire.get_numero_compte()}.")
        else:
            print("Opération impossible : Solde insuffisant.")

    def get_numero_compte(self):
        return self.__numero_compte



compte1 = CompteBancaire(numero_compte="123456", nom="Dupont", prenom="Alice", solde_initial=1000)


compte1.afficher()
compte1.retrait(500)
compte1.versement(200)
compte1.afficher_solde()


compte2 = CompteBancaire(numero_compte="789012", nom="Martin", prenom="Bob", solde_initial=-200, decouvert=True)

compte2.afficher()
compte1.virement(compte_destinataire=compte2, montant=300)
compte2.afficher_solde()
