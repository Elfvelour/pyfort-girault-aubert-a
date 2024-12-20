from random import *
import json
def charger_enigmes(fichier:str):
    with open(fichier,'r', encoding='utf8') as f:
        donnees = json.load(f)
        return donnees

FICHIER = "./data/enigmesPF.json"

def mot_miniscule(mot):
    L = list(mot)
    mot_min = ''
    for i in range(len(L)):
        if ord(L[i]) > 62 and ord(L[i]) < 95:
            L[i] = chr(ord(L[i]) + 32)
    for i in range(len(L)):
        mot_min = mot_min + L[i]
    return mot_min

liste_pere_fouras=["Ah, ce n'est pas la bonne réponse... le trésor reste hors de portée pour l'instant !",
"Mauvaise pioche, mon cher aventurier, il va falloir faire mieux pour mériter vos clés.",
"Ah, vous êtes tombé dans mon piège... c'est un échec !",
"La réponse était pourtant devant vos yeux, mais la clef restera ici, hihihi !",
"Non, non, non ! Vous n’avez pas percé les mystères de mon énigme !",
"Je vois que vous confondez sagesse et précipitation... réfléchissez davantage la prochaine fois !",
"Vous pensiez me piéger ? Hélas, c’est moi qui vous tiens !",
"Ah, si seulement vos réponses étaient aussi justes que votre enthousiasme...",
"L’esprit est fort, mais l'énigme était plus rusée, hihihi !",
"Retournez donc voir Passe-Partout, il vous consolera mieux que moi !"]

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
            print(liste_pere_fouras[randint(0,len(liste_pere_fouras)-1)])
            print("Ils vous restent : ",nombre_essais,"nombres d'essai(s)")
    if nombre_essais<1:
        print("Vous avez échoué, la solution était",enigme["reponse"])
        return False
print(enigmes_pere_fouras())
