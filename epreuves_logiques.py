mat = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

partie = True

def afficher_mat():
    for ligne in mat:
        print(ligne)
    print()

def jouer(joueur):
    afficher_mat()
    symbole = 'X' if joueur == 1 else 'O'
    print(f"Joueur {joueur} ({symbole}), à vous de jouer !")
    changer= (input("Indiquez la position (1-3) : ")).split(",")
    l_changer = int(changer[0])-1
    c_changer = int(changer[1])-1
    if mat[l_changer][c_changer] == " ":
            mat[l_changer][c_changer] = symbole

    else:
        print("Cette case est déjà prise. Essayez à nouveau.")

def verifier_victoire(symbole):
    for i in range(3):
        if mat[i][0] == mat[i][1] == mat[i][2] == symbole:
            return True
        if mat[0][i] == mat[1][i] == mat[2][i] == symbole:
            return True
    if mat[0][0] == mat[1][1] == mat[2][2] == symbole:
        return True
    if mat[0][2] == mat[1][1] == mat[2][0] == symbole:
        return True
    return False

def verifier_match_nul():
    for ligne in mat:
        if " " in ligne:
            return False
    return True