class Tache:
    def __init__(self, titre, description, statut="À faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"Tâche '{self.titre}' - {self.description} - Statut : {self.statut}"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouter_tache(self, tache):
        self.taches.append(tache)
        print(f"Tâche '{tache.titre}' ajoutée à la liste.")

    def supprimer_tache(self, titre_tache):
        for tache in self.taches:
            if tache.titre == titre_tache:
                self.taches.remove(tache)
                print(f"Tâche '{tache.titre}' supprimée de la liste.")
                return
        print(f"Tâche '{titre_tache}' non trouvée dans la liste.")

    def marquer_comme_finie(self, titre_tache):
        for tache in self.taches:
            if tache.titre == titre_tache:
                tache.statut = "Terminée"
                print(f"Tâche '{tache.titre}' marquée comme terminée.")
                return
        print(f"Tâche '{titre_tache}' non trouvée dans la liste.")

    def afficher_liste(self):
        print("Liste des tâches:")
        for tache in self.taches:
            print(tache)

    def filter_liste(self, statut_filter):
        filtered_list = [tache for tache in self.taches if tache.statut == statut_filter]
        print(f"Tâches avec le statut '{statut_filter}':")
        for tache in filtered_list:
            print(tache)


tache1 = Tache("Faire les courses", "Acheter des fruits et légumes")
tache2 = Tache("Réviser pour l'examen", "Chapitres 5 à 10")
tache3 = Tache("Faire du sport", "Jogging pendant 30 minutes")

liste_taches = ListeDeTaches()

liste_taches.ajouter_tache(tache1)
liste_taches.ajouter_tache(tache2)
liste_taches.ajouter_tache(tache3)

liste_taches.afficher_liste()

liste_taches.marquer_comme_finie("Faire du sport")

liste_taches.filter_liste("À faire")

liste_taches.supprimer_tache("Réviser pour l'examen")

liste_taches.afficher_liste()
