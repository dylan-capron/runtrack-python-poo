class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informations_vehicule(self):
        print(f"Marque: {self.marque}")
        print(f"Modèle: {self.modele}")
        print(f"Année: {self.annee}")
        print(f"Prix: {self.prix} €")

    def demarrer(self):
        print("Attention, je roule")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informations_vehicule(self):
        super().informations_vehicule()
        print(f"Nombre de portes: {self.portes}")

    def demarrer(self):
        print("Attention, je roule.")


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roues=2):
        super().__init__(marque, modele, annee, prix)
        self.roues = roues

    def informations_vehicule(self):
        super().informations_vehicule()
        print(f"Nombre de roues: {self.roues}")

    def demarrer(self):
        print("Attention, je roule.")


voiture = Voiture(marque="Toyota", modele="Corolla", annee=2022, prix=25000)
voiture.informations_vehicule()
voiture.demarrer()

moto = Moto(marque="Harley-Davidson", modele="Sportster", annee=2022, prix=12000)
moto.informations_vehicule()
moto.demarrer()
