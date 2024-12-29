##############################################
###### Auteur : Thomas AUBERT ################
##############################################

import random

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

def est_entree_valide(entree):
    if len(entree) != 2:
        return False
    for x in entree:
        if len(x) == 0 or any(c not in "0123456789" for c in x) or int(x) <= 0:
            return False
    return True

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

def verifier_victoire(grille, symbole):

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

    cpt_col=0
    for j in range(taille):
        cpt_col=0
        for i in range(taille):
            if grille[i][j] == symbole:
                cpt_col+=1
        if cpt_col==3:
            return True

    cpt_diag=0
    for i in range(taille):
        if grille[i][i]==symbole:
            cpt_diag+=1
    if cpt_diag==3:
        return True

    cpt_anti_diag=0
    for i in range(taille):
        if grille[i][taille - 1 - i] == symbole:
            cpt_anti_diag+=1
    if cpt_anti_diag==3:
        return True

    return False

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

def verifier_resultat(grille):
    if verifier_victoire(grille, "X"):
        return "joueur"

    if verifier_victoire(grille, "O"):
        return "maitre"

    for ligne in grille:
        if " " in ligne:
            return False
    return "nul"

def coup_maitre(grille,symbole):

    coup_dispo=[]
    for i in range(len(grille)):
        for j in range(len(grille)):
            if grille[i][j]==" ":
                coup_dispo.append((i,j))

    for coup in coup_dispo:
        x, y = coup
        grille[x][y] = symbole
        if verifier_victoire(grille, symbole):
            grille[x][y] = " "
            return coup
        grille[x][y] = " "

    symbole_adversaire='X'
    for coup in coup_dispo:
        x, y = coup
        grille[x][y] = symbole_adversaire
        if verifier_victoire(grille, symbole_adversaire):
            grille[x][y] = " "
            return coup
        grille[x][y] = " "

    return random.choice(coup_dispo)

def tour_maitre(grille):
    coup = coup_maitre(grille, "O")
    grille[coup[0]][coup[1]] = 'O'

def jeu_tictactoe():
    grille = [[" " for _ in range(3)] for _ in range(3)]
    afficher_grille(grille)

    while True:
        print("Tour du maître :")
        tour_maitre(grille)
        afficher_grille(grille)
        resultat = verifier_resultat(grille)
        if resultat:
            if resultat == "maitre":
                print("Le maître a gagné ! Nullos U_U")
            elif resultat == "nul":
                print("Match nul *^____^*")
            break

        print("Tour du joueur :")
        tour_joueur(grille)
        afficher_grille(grille)
        resultat = verifier_resultat(grille)
        if resultat:
            if resultat == "joueur":
                print("Le joueur a gagné ! GG EZ")
            elif resultat == "nul":
                print("Match nul *^____^*")
            break

