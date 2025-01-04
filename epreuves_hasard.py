##############################################
###### Programme Python epreuve hasard  ######
###### Auteur: Timothée Girault         ######
###### Version: 1.1                     ######
##############################################

##############################################
# Importations des fonctions externes

from random import *

##############################################
# Déclaration des fonctions utilisateurs

#demande aux joueurs de trouver la clé sous 3 lettres parmi A,B,C et renvoie vrai ou faux en fonction de la réponse finale du joueur
def bonneteau():
    tentative=1
    liste=['A','B','C']
    print("Bienvenue au jeu du bonneteau,\nles règles sont simples. Vous avez\n2 tentatives pour trouver la clé\nparmi 3 choix: A, B ou C")
    print("-------------------------------------")
    #boucle while qui permet de savoir la réponse de l'utilisateur et de le comparer à la solution choisi au hasard
    while tentative<3:
        solution = liste[randint(0, 2)]
        print("Il vous reste :",3-tentative,"tentative(s)")
        choix_joueur = str(input("Choisir un bonneteau: A, B ou C : "))
        #change la réponse en majuscule et vérifie bien que la réponse soit A,B ou C
        choix_joueur=choix_joueur.upper()
        while choix_joueur!='A'and choix_joueur!='B'and choix_joueur!='C':
            choix_joueur=str(input("Choisir un bonneteau: A, B ou C : "))
        #compare la réponse à la solution, incrémente la tentative, dit qu'il a faux ou pas et
        # renvoie la solution s'il n'a pas trouvé
        if choix_joueur==solution:
           print("Vous avez trouvez la clé")
           return True
        else:
            if tentative==2:
                print("La clé était sous la lettre", solution)
                return False
            else:
                print("Vous n'avez pas trouver la clé")
                print("-------------------------------------")
                tentative+=1

#demande au joueur de lancer les dés et renvoie s'il a gagné ou non par vrai ou faux
def lance_de_des():
    essais=3
    #boucle while pour lancer le jeu et déterminer qui a gagner entre le joueur et le maitre du jeu
    while essais>0:
        #lance la partie du joueur, lance ses dés et détermine s'il a gagné ou non pour passer au tour du maitre du jeu
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
            #verfie si le maitre du jeu à gagner, incrémente les essais et retourne faux s'il y a match nul
            if des_maitre_du_jeu[0]==6 or des_maitre_du_jeu[1]==6:
                print("Le maître du jeu a remporté la clé")
                return False
            else:
                if essais == 1:
                    print("Après trois essais, aucun des joueurs n'a gagné, c'est un match nul")
                    return False
                else:
                    print("On passe au prochain essai!")
                    print("---------------------------")
                    essais=essais-1

##############################################
# Corps du programme principal

#récupère les 2 épreuves et en choisi une au hasard en lançant cette épreuve
def epreuve_hasard()->bool:
    epreuve=[lance_de_des,bonneteau]
    aleatoire=randint(0,1)
    epreuve=epreuve[aleatoire]
    return epreuve()
