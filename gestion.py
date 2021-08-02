# Programme écrit par Lorenzo Culianez
# coding: utf-8
import os
# Gestion de la date
from datetime import datetime
from datetime import date

# Déclaration du nombre de parcelles
NombreParcelles = 0

#Déclaration des
def CreationParcelle():
    NombreParcelles = NombreParcelles + 1
    print("Vous avez créé une parcelle. Vous avez", NombreParcelles, "parcelles")
    print("Voulez-vous nommer votre parcelle? o/n")
    NomParcelle = input()


def NommageParcelle():
    if NomParcelle1 == "o":
        NomParcelle1 = input("Comment Souhaitez vous la nommer? :")
        print("Votre parcelle s'appelle", NomParcelle1)
    elif NomParcelle1 == "n":
        NomParcelle1 = "Parcelle 1"
        print("Votre parcelle a été nommée par défaut :", NomParcelle1)
    else:
        NomParcelle1 = '¨Parcelle 1'

"""
    légumes fleur
    légumes_feuilles
    légumes_fruits
    légumes_bulbe
    légumes_tubercules
    légumes_graines
    légumes_racine
    légumes_tiges"""

DateActuelle = date.today()
# Aujourdhui = datetime.strptime(DateActuelle, "%m/%d/%Y")


CreationParcelle = 0

# Stockage du nom du jardinier
Nom_jardinier = input("Comment vous appelez vous? : ")

# Phrase d'accueil et menu
print("Bonjour", Nom_jardinier)
print("Aujourd'hui nous sommes le", DateActuelle)  # Aujourdhui)
print("Vous avez actuellement", NombreParcelles, "parcelles")

# choix de création/consultation des parcelles
while NombreParcelles <= 0:
    print("voulez vous créer une parcelle? o/n")
    CreationParcelle = input()
    if CreationParcelle == "o":
        CreationParcelle()
    elif CreationParcelle == "n":
        print("Vous avez choisit de ne pas créer de parcelle")
    else:
        print("Merci de bien vouloir choisir entre Oui 'o' ou Non 'n'")
else:
    print("Que souhaitez vous faire? : ")
    print("1) Créer une parcelle")
    print("2) Consulter une parcelle")
    print("3) Gérer une parcelle")
    choixmenu = input()
    print(choixmenu)
    if choixmenu == "1":
        NombreParcelles = NombreParcelles + 1
        print("Vous avez créé une parcelle. Vous avez", NombreParcelles, "parcelles")
        print("Voulez-vous nommer votre parcelle? o/n")
        NomParcelle = input()
    elif choixmenu == "2":
        print("Quelle parcelle souhaitez vous consulter?")
    elif choixmenu == "3":
        print("Quelle parcelle souhaitez vous gérer?")
    else:
        print("Merci de bien vouloir choisir une option valide")

# Preparation de l’arret
os.system("pause")
