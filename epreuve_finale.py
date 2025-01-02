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

# Fonction qui lance le jeu finale pour trouvé un mot secret à l'aide de 5 indices
def salle_DE_Tresor(fichier:str):
    with open(fichier,'r',encoding='utf8') as f:
        jeux_tv= json.load(f)

        jeux_tv=jeux_tv['Fort Boyard']
        #j'obtient toute les années et je les mets en liste
        liste_jeux_tv=list(jeux_tv.keys())
        annee=choice(liste_jeux_tv)
        jeux_tv = jeux_tv[annee]
        #j'ai toute la liste des emissions et je met leurs clé en liste
        liste_emission=list(jeux_tv.keys())
        emission=choice(liste_emission)
        jeux_tv = jeux_tv[emission]
        #j'obtient l'émission avec les indices et le mot codé
        indice=jeux_tv['Indices']
        mot_code=jeux_tv['MOT-CODE']
        k=2

        print("Voici les 3 premiers indices :\n"+indice[0]+'\n'+indice[1]+'\n'+indice[2])
        essais=3
        reponse_correcte = False
        while essais>0:
            reponse_joueur=str(input("Saisir une réponse : "))
            if mot_miniscule(reponse_joueur)==mot_miniscule(mot_code):
                reponse_correcte=True
                essais=0
            else:
                essais=essais-1
                if essais>0:
                    k+=1
                    print("Ils vous restent : ",essais,"tentative(s)")
                    print("Voici un indice suplémentaire : \n"+indice[k])
                else:
                    print("Le code secret était : ",mot_code)
        if reponse_correcte==True:
            print("Vous avez gagné !")
        else:
            print("Vous avez perdu, bande de vilains et malhonnêtes élèves!")
            #réference aux remarques de mon ancien prof de maths expertes Mr Candapin


#chemin du fichier indicesSalle.json pour la fonction au-dessus
FICHIER="./data/indicesSalle.json"

