class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficher_age(self):
        print(f"L'âge de la personne est de {self.age} ans.")

    def bonjour(self):
        print("Hello")

    def modifier_age(self, nouvel_age):
        self.age = nouvel_age
        print(f"L'âge de la personne a été modifié à {nouvel_age} ans.")


class Eleve(Personne):
    def aller_en_cours(self):
        print("Je vais en cours.")

    def afficher_age(self):
        print(f"J'ai {self.age} ans.")


class Professeur(Personne):
    def __init__(self, age=14, matiere_enseignee="Inconnue"):
        super().__init__(age)
        self.matiere_enseignee = matiere_enseignee

    def enseigner(self):
        print("Le cours va commencer.")


eleve = Eleve()
eleve.modifier_age(15) 
eleve.bonjour()  
eleve.aller_en_cours()  

professeur = Professeur(age=40)
professeur.bonjour()  
professeur.enseigner()  
