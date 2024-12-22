##############################################
###### Programme Python epreuve hasard  ######
###### Auteur: Timothée Girault         ######
###### Version: 1.0                     ######
##############################################

##############################################
# Importations des fonctions externes

from random import *

##############################################
# Déclaration de fonctions utilisateurs

def bonneteau():
    tentative=1
    variable=''
    cle=False
    liste=['A','B','C']
    print("Bienvenue au jeux du bonneteau,\nles règles sont simples. Vous avez\n2 tentatives pour trouver la clé\nparmi 3 chois: A, B ou C")
    print("-------------------------------------")
    while tentative<3:
        variable=liste[randint(0,2)]
        print("Il reste :",3-tentative,"tentative(s)")
        choix_joueur = str(input("Choisir un bonneteau: A, B ou C : "))
        while choix_joueur!='A'and choix_joueur!='B'and choix_joueur!='C':
            choix_joueur=str(input("Choisir un bonneteau: A, B ou C : "))
        if choix_joueur==variable:
           print("Vous avez trouvez la clé")
           tentative=3
           cle=True
        else:
           print("Vous n'avez pas trouver la clé")
           tentative+=1
    if cle:
        return True
    else:
        print("La clé était sous la lettre",variable)
        return False

def lance_de_des():
    essais=3
    while essais>0:
        print("Le nombre d'essai(s) restant(s) est : ",essais,"essai(s)")
        input("Lancer les dés en appuyant sur la touche 'Entrée' : ")
        des_joueur= (randint(1, 6), randint(1, 6))
        print("Le 1er dé est : ",des_joueur[0]," et le 2ème dé est : ",des_joueur[1])
        if des_joueur[0]==6 or des_joueur[1]==6:
            print("Vous avez remporté la clé")
            return True
        else:
            print("-------------------------------")
            print("C'est au tour du maître du jeu")
            des_maitre_du_jeu = (randint(1, 6), randint(1, 6))
            print("Le 1er dé est : ", des_maitre_du_jeu[0], " et le 2ème dé est : ", des_maitre_du_jeu[1])
            if des_maitre_du_jeu[0]==6 or des_maitre_du_jeu[1]==6:
                print("Le maître du jeu a remporté la clé")
                return False
            else:
                print("On passe au prochain essai!")
                print("---------------------------")
                essais=essais-1
    if essais==0:
        print("Après trois essais, aucun des joueurs n'a gagné, c'est un match nul")
        return False

##############################################
# Corps du programme principal

#récupère les 2 épreuves et en choisi un au hasard en lançant cette épreuve
def epreuve_hasard()->bool:
    epreuve=[lance_de_des,bonneteau]
    aleatoire=randint(0,1)
    epreuve=epreuve[aleatoire]
    return epreuve()