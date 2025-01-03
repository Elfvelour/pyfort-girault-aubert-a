##############################################
###### Programme Python epreuve finale  ######
###### Auteur: Timothée Girault         ######
###### Version: 1.2                     ######
##############################################

##############################################
# Importation des fonctions externes

import json
from random import *
from fonctions_utiles import *

##############################################
# Déclaration des fonctions utilisateurs

# Fonction qui lance le jeu finale pour trouver un mot secret à l'aide de 5 indices
def salle_DE_Tresor(fichier:str):
    #On ouvre le fichier et on télécharge l'intégralité du texte sur jeux_tv
    with open(fichier,'r',encoding='utf8') as f:
        jeux_tv= json.load(f)

        jeux_tv=jeux_tv['Fort Boyard']
        #On obtient la liste de toute les années et on les mets dans la liste liste_jeux_tv
        liste_jeux_tv=list(jeux_tv.keys())
        #On choisi au hasard une année
        annee=choice(liste_jeux_tv)
        jeux_tv = jeux_tv[annee]
        #On obtient toute la liste des emissions et on met leurs clé dans la liste liste_emission
        liste_emission=list(jeux_tv.keys())
        #On choisi au hasard une émission
        emission=choice(liste_emission)
        jeux_tv = jeux_tv[emission]
        #On obtient l'émission dans la variable jeux_tv avec les indices et le mot codé
        # qu'on assigne aux variables indice et mot_code
        indice=jeux_tv['Indices']
        mot_code=jeux_tv['MOT-CODE']

        print("Voici les 3 premiers indices :\n"+indice[0]+'\n'+indice[1]+'\n'+indice[2])
        print("--------------------------------------------")
        essais=3
        reponse_correcte = False
        #boucle while qui compare la réponse du joueur et de la solution, décrémente les essais, renvoie un indice supplémentaire
        # si échec et renvoie la solution si le joueur ne le trouve en 3 essais avec 5 indices en tout
        while essais>0:
            reponse_joueur=str(input("Saisir une réponse : "))
            if mot_miniscule(reponse_joueur)==mot_miniscule(mot_code):
                reponse_correcte=True
                essais=0
            else:
                essais=essais-1
                if essais>0:
                    print("Ils vous restent : ",essais,"tentative(s)")
                    print("Voici un indice suplémentaire : \n"+indice[3+essais])
                    print("--------------------------------------------")
                else:
                    print("Le code secret était : ",mot_code)
        # si le joueur a gagné on renvoie qu'il a gagné sinon le contraire en renvoyant qu'il a perdu
        if reponse_correcte==True:
            print("Vous avez gagné!")
        else:
            print("Vous avez perdu!")

#chemin du fichier indicesSalle.json pour la fonction au-dessus
FICHIER="./data/indicesSalle.json"

