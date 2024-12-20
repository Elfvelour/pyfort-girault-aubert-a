from random import *
import json
def charger_enigmes():
    with open('enigmesPF.json','r', encoding='utf8') as f:
        donnees = json.load(f)
        return donnees
print(charger_enigmes())

def enigmes_pere_fouras():
    enigme=[]
    enigme=randint(charger_enigmes())
    nombre_essais=3
    print(enigme[:])
    while nombre_essais>0:
        reponse_joueur = str(input("Saisir une réponse : "))
        L = list(reponse_joueur)
        reponse_joueur_min = ''
        for i in range(len(L)):
            if ord(L[i]) > 62:
                L[i] = chr(ord(L[i]) + 32)
        for i in range(len(L)):
            reponse_joueur_min = reponse_joueur_min + L[i]
        if reponse_joueur_min == enigme["reponse"]:
            print("La clé est trouvé, bravo les ptits indiens")
            return True
        else:
            nombre_essais=nombre_essais-1
            print("Ils vous restent : ",nombre_essais,"nombres d'essai(s)")
    if nombre_essais<1:
        print("Vous avez échoué, la solution était",enigme["reponse"])
        return False
