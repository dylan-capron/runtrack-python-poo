class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1
    
    def nommer(self, nom):
        self.prenom = nom
        print(f"L'animal s'appelle {self.prenom}.")

animal_instance = Animal()

print("L'âge initial de l'animal est de", animal_instance.age, "ans.")

animal_instance.vieillir()

print("L'animal a vieilli de", animal_instance.age,"an.")

animal_instance.nommer("Ruby")

