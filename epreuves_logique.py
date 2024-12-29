############################################
####         Projet Fort Boyard         ####
####        Auteur : Thomas AUBERT      ####
####       Est une épreuve du projet    ####
############################################

import random #utile pour le coup du maître

#permet l'affichage de la grille du morpion. La fonction renvoie un tableau 3x3
def afficher_grille(grille):
    print('----------------')
    for i in range(len(grille)):
        print("| ",end=' ')
        for j in range(len(grille[0])):
            print(grille[i][j]+" | ", end=" ")
        print('\t')
        if i!=j:
            print('----------------')
    print('----------------')
    return grille

#Permet de vérifier si les coordonnées entreés par le joueur sont correctes. Renvoie un booléen.
def est_entree_valide(entree):
    if len(entree) != 2:
        return False
    for x in entree:
        if len(x) == 0 or any(c not in "0123456789" for c in x) or int(x) <= 0:
            return False
    return True

#Il s'agit du déroulement du tour du joueur. C'est à dire entrer les coordonnées où il veut jouer.
#Ne renvoie rien car on a pas besoin de récupérer une variable à la fin.
def tour_joueur(grille):
    valide = False
    while not valide:
        pos = input("Saisir les coordonnées du symbole (ex: 1,2) : ").split(",")
        if est_entree_valide(pos):
            l, c = int(pos[0]) - 1, int(pos[1]) - 1
            if 0 <= l < len(grille) and 0 <= c < len(grille[0]) and grille[l][c] == " ":
                grille[l][c] = "X"
                valide = True
            else:
                print("Case invalide ou déjà occupée. Réessayez.")
        else:
            print("Entrée invalide. Assurez-vous d'entrer deux chiffres séparés par une virgule.")

#S'occupe de vérifier s'il y a une victoire. Prend donc en paramètre un symbole pour lequel il vérifie s'il y a victoire.
#Renvoie un booléen
def verifier_victoire(grille, symbole):

    #vérifie s'il y a une victoire sur les lignes
    taille = len(grille)
    cpt_ligne=0
    for i in range(taille):
        victoire_ligne = False
        cpt_ligne=0
        for j in range(taille):
            if grille[i][j] == symbole:
                cpt_ligne+=1
        if cpt_ligne==3:
            return True

    #vérifie s'il y a une victoire sur les colonnes
    cpt_col=0
    for j in range(taille):
        cpt_col=0
        for i in range(taille):
            if grille[i][j] == symbole:
                cpt_col+=1
        if cpt_col==3:
            return True

    #Vérifie s'il y a une victoire sur la diagonale principale.
    cpt_diag=0
    for i in range(taille):
        if grille[i][i]==symbole:
            cpt_diag+=1
    if cpt_diag==3:
        return True

    #Vérifie s'il y a une victoire sur la diagonale secondaire.
    cpt_anti_diag=0
    for i in range(taille):
        if grille[i][taille - 1 - i] == symbole:
            cpt_anti_diag+=1
    if cpt_anti_diag==3:
        return True

    return False

#la fonction s'occupe de regarder si la grille est complète où s'il y a encore de la place.
def grille_complete(grille):
    cpt=0
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j] != " ":
                cpt+=1
            else:
                return False
    if cpt==9:
        return True

#Vérifie s'il y a une victoire sur la grille. Et s'il y a une victoire, la fonction renvoie qui a gagné.
def verifier_resultat(grille):
    if verifier_victoire(grille, "X"):
        return "joueur"

    if verifier_victoire(grille, "O"):
        return "maitre"

    for ligne in grille:
        if " " in ligne:
            return False
    return "nul"

#S'occupe de trouver un coup à jouer pour le maître. Elle renvoie donc un tuple.
def coup_maitre(grille,symbole):

    #On commence par récupérer tous les coups disponibles sur la grille.
    coup_dispo=[]
    for i in range(len(grille)):
        for j in range(len(grille)):
            if grille[i][j]==" ":
                coup_dispo.append((i,j))

    #On regarde si un de coup est gagnant pour le maître
    for coup in coup_dispo:
        x, y = coup
        grille[x][y] = symbole
        if verifier_victoire(grille, symbole):
            grille[x][y] = " "
            return coup
        grille[x][y] = " "

    #On regarde si un coup est gagnant pour l'adversaire. (Sert pour bloquer le joueur)
    symbole_adversaire='X'
    for coup in coup_dispo:
        x, y = coup
        grille[x][y] = symbole_adversaire
        if verifier_victoire(grille, symbole_adversaire):
            grille[x][y] = " "
            return coup
        grille[x][y] = " "

    #Si on ne peut pas gagner ou bloquer. On joue un coup choisi au hasard.
    return random.choice(coup_dispo)

#Permet de faire jouer le maôtre sur la grille.
def tour_maitre(grille):
    coup = coup_maitre(grille, "O")
    grille[coup[0]][coup[1]] = 'O'

#S'occupe du déroulement du jeu. La fonction ne renvoie rien car on a pas besoin de récupérer d'informations.
def jeu_tictactoe():
    grille = [[" " for _ in range(3)] for _ in range(3)] #création de la grille
    afficher_grille(grille)

    #déroulement de la partie
    while True:
        #On fait jouer le maître
        print("Tour du maître :")
        tour_maitre(grille)
        afficher_grille(grille)
        resultat = verifier_resultat(grille)
        if resultat: #on regarde si le maître a gagné :
            if resultat == "maitre":
                print("Le maître a gagné ! Nullos U_U")
            elif resultat == "nul":
                print("Match nul *^____^*")
            break

        #On fait jouer le joueur.
        print("Tour du joueur :")
        tour_joueur(grille)
        afficher_grille(grille)
        resultat = verifier_resultat(grille)
        if resultat: #On regarde si le joueur a gagné.
            if resultat == "joueur":
                print("Le joueur a gagné ! GG EZ")
            elif resultat == "nul":
                print("Match nul *^____^*")
            break

