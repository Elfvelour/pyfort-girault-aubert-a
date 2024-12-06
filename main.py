from epreuves_logique import *

partie = True
while partie:
    jouer(1)
    if verifier_victoire('X'):
        afficher_mat()
        print("Le joueur 1 (X) a gagné !")
        partie = False
        break
    if verifier_match_nul():
        afficher_mat()
        print("Match nul !")
        partie = False
        break
    jouer(2)
    if verifier_victoire('O'):
        afficher_mat()
        print("Le joueur 2 (O) a gagné !")
        partie = False
        break
    if verifier_match_nul():
        afficher_mat()
        print("Match nul !")
        partie = False
        break