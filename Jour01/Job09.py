class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        prixTTC = self.prixHT * (1 + self.TVA)
        return prixTTC

    def obtenirInformations(self):
        infos = f"Informations du produit - Nom: {self.nom}, Prix HT: {self.prixHT}, TVA: {self.TVA * 100}%"
        return infos

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA

produit1 = Produit(nom="Produit1", prixHT=20, TVA=0.20)
produit2 = Produit(nom="Produit2", prixHT=30, TVA=0.15)

infos_produit1 = produit1.obtenirInformations()
prix_TTC_produit1 = produit1.calculerPrixTTC()

infos_produit2 = produit2.obtenirInformations()
prix_TTC_produit2 = produit2.calculerPrixTTC()

produit1.modifierNom("NouveauProduit1")
produit1.modifierPrixHT(25)

produit2.modifierNom("NouveauProduit2")
produit2.modifierPrixHT(35)

nouvelles_infos_produit1 = produit1.obtenirInformations()
nouveau_prix_TTC_produit1 = produit1.calculerPrixTTC()

nouvelles_infos_produit2 = produit2.obtenirInformations()
nouveau_prix_TTC_produit2 = produit2.calculerPrixTTC()

print(infos_produit1)
print(f"Prix TTC : {prix_TTC_produit1}\n")

print(infos_produit2)
print(f"Prix TTC : {prix_TTC_produit2}\n")

print(nouvelles_infos_produit1)
print(f"Nouveau prix TTC : {nouveau_prix_TTC_produit1}\n")

print(nouvelles_infos_produit2)
print(f"Nouveau prix TTC : {nouveau_prix_TTC_produit2}\n")