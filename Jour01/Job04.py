class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je m'appelle {self.prenom} {self.nom}"

personne1 = Personne(nom="Dorie", prenom="John")
personne2 = Personne(nom="Jones", prenom="Morgan")
personne3 = Personne(nom="Clark", prenom="Alicia")
personne4 = Personne(nom="Galvez", prenom="Luciana")

print(personne1.SePresenter())
print(personne2.SePresenter())
print(personne3.SePresenter())
print(personne4.SePresenter())