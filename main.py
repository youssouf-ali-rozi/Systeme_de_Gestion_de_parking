#Auteurs : Oumou Tabara Diallo et Youssouf Ali Rozi

# --- Configuration initiale ---
# Créer des véhicules
from Abonnement import Abonnement
from Acces import Acces
from Client import Client
from Panneau_Affichage import Panneau_Affichage
from Parking import Parking
from Place import Place
from Voiture import Voiture

voiture1 = Voiture(2.0, 4.0, "AB-123-CD")
voiture2 = Voiture(1.8, 4.2, "XY-987-ZT")

# Créer des places de parking
place1 = Place(numero=1, niveau='A', longueur=4.0, hauteur=2.0)
place2 = Place(numero=2, niveau='A', longueur=4.2, hauteur=1.8)

# Créer un parking avec des places disponibles
parking = Parking(nbplace=5, prix=10)
parking.ajouterPlace(place1)
parking.ajouterPlace(place2)
#parking.collectionPlaceDispo = [place1, place2]

# Créer des clients
client_non_abonne = Client("Youssouf ali","1 jkdll", voiture1)
client_abonne = Client("Oumou tabara","2 fgdhj", voiture2)
abonnement= Abonnement("Annuelle", 300)

client_abonne.sAbonner(abonnement)

# Créer un accès au parking
acces = Acces()

# --- Cas 1 : Client non abonné ---
print("---- Cas 1 : Client non abonné ----")
resultat1 = acces.lancerProcedureEntree(client_non_abonne, parking)
print(resultat1)

# --- Cas 2 : Client abonné ---
print("\n---- Cas 2 : Client abonné ----")
resultat2 = acces.lancerProcedureEntree(client_abonne, parking)
print(resultat2)

# --- Tests supplémentaires ---
# Vérification des places restantes après les entrées
print("\n--- État du parking ---")
print(acces.Panneau_Affichage.afficherNbPlacesDisponibles(parking))


