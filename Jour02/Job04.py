class Student:
    def __init__(self, nom, prenom, numero_etudiant, credits=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = credits
        self.__level = self.__student_eval()  

    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_numero_etudiant(self):
        return self.__numero_etudiant

    def get_credits(self):
        return self.__credits

    def get_level(self):
        return self.__level

    def add_credits(self, nombre_credits):
        if nombre_credits > 0:
            self.__credits += nombre_credits
            self.__level = self.__student_eval()  
            print(f"Le nombre de crédits de {self.__prenom} {self.__nom} est de {self.__credits} points.")
        else:
            print("Erreur : Le nombre de crédits doit être supérieur à zéro.")

    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        print(f"Informations de l'étudiant {self.__prenom} {self.__nom} (ID {self.__numero_etudiant}):")
        print(f"Nombre de crédits : {self.__credits}")
        print(f"Niveau : {self.__level}")

john_doe = Student(nom="Doe", prenom="John", numero_etudiant=145)

john_doe.add_credits(10)
john_doe.add_credits(20)
john_doe.add_credits(30)

john_doe.student_info()
