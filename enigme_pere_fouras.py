##############################################
####### Programme Python enigme Fouras #######
####### Auteur: Timothée Girault       #######
####### Version: 1.3                   #######
##############################################

##############################################
# Importation des fonctions externes

from fonctions_utiles import *
from random import *
import json

##############################################
# Listes de réponses du Père Fouras

# Mauvaise réponse du joueur et le Père Fourars lui répond par une petite pique
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

# Bonne réponse du joueur et le Père Fouras lui répond en le taquinant
liste_felicitation_fouras=["Hihihi, voilà qui est étonnant... je pensais que vous alliez échouer !",
"Une victoire éclatante, mais ne prenez pas trop confiance... mes énigmes se corsent !",
"Vous êtes aussi rusé qu’un renard... ou ai-je simplement été trop généreux ?",
"Hé bien, vous avez réussi ! Allez vite chercher votre clé avant que je change d’avis.",
"C’est une victoire méritée, aventurier. Mais attention, le Fort n’a pas dit son dernier mot."]

##############################################
# Déclarations des fonctions utilisateurs

# Ouvre le fichier enigmePF.json et renvoie l'intégralité du texte compris dans le fichier
def charger_enigmes(fichier:str):
    with open(fichier,'r', encoding='utf8') as f:
        donnees = json.load(f)
        return donnees

#chemin du fichier enigmePF.json pour la fonction au dessus
FICHIER = "./data/enigmesPF.json"

# Fonction qui utilise la fonction au-dessus pour afficher et faire deviner des enigmes
def enigmes_pere_fouras():
    donnees=charger_enigmes("./data/enigmesPF.json")
    enigme=[]
    enigme=donnees[randint(0,len(donnees)-1)]
    print("La question est :",'\n')
    print(enigme['question'],'\n')
    nombre_essais=3
    while nombre_essais>0:
        reponse_joueur = str(input("Saisir une réponse : "))
        reponse_joueur_min=mot_miniscule(reponse_joueur)
        reponse_enigme=mot_miniscule(enigme["reponse"])
        if reponse_joueur_min == reponse_enigme:
            print("La clé est trouvé, bravo ")
            print(liste_felicitation_fouras[randint(0,len(liste_felicitation_fouras)-1)])
            return True
        else:
            nombre_essais=nombre_essais-1
            print(liste_pere_fouras[randint(0,len(liste_pere_fouras)-1)])
            print("PS: n'oubliez pas le 'le' ou 'la devant le mot'")
            print("Ils vous restent : ",nombre_essais,"nombres d'essai(s)\n")
    if nombre_essais<1:
        print("Vous avez échoué, bande de nullos,la solution était",enigme["reponse"])
        return False
