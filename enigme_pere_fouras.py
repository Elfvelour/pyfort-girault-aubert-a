from fonctions_utiles import *
from random import *
import json
def charger_enigmes(fichier:str):
    with open(fichier,'r', encoding='utf8') as f:
        donnees = json.load(f)
        return donnees

FICHIER = "./data/enigmesPF.json"

def enigmes_pere_fouras():
    donnees=charger_enigmes("./data/enigmesPF.json")
    enigme=[]
    enigme=donnees[randint(0,len(donnees))]
    print(enigme)
    print("La question est :",'\n')
    print(enigme['question'])
    nombre_essais=3
    while nombre_essais>0:
        reponse_joueur = str(input("Saisir une réponse : "))
        reponse_joueur_min=mot_miniscule(reponse_joueur)
        reponse_enigme=mot_miniscule(enigme["reponse"])
        if reponse_joueur_min == reponse_enigme:
            print("La clé est trouvé, bravo les ptits indiens")
            return True
        else:
            nombre_essais=nombre_essais-1
            print("Ils vous restent : ",nombre_essais,"nombres d'essai(s)")
    if nombre_essais<1:
        print("Vous avez échoué, la solution était",enigme["reponse"])
        return False
print(enigmes_pere_fouras())
