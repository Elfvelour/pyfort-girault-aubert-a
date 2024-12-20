from  math import sqrt
from random import randint

#epreuve 1 de maths, les factorielles
def factorielle(n):
    res=1
    if n==0:
        res=1
    else:
        for i in range(n,1,-1):
            res=res*i
    return res

def epreuve_factorielle():
    n=randint(1,10)
    res=factorielle(n)
    print("Épreuve de Mathématiques: Calculer la factorielle de ",n)
    resultat=int(input("Votre réponse : "))
    if resultat==res:
        return True
    else:
        return False

#epreuve 2, les nombres premiers
def est_premier(n):
    premier = True
    for i in range(2, int(sqrt(n))+ 1):
        if n % i == 0:
            premier = False
    return premier

def premier_plus_proche(n):
    trouve=False
    nombre=n
    while not trouve:
        if est_premier(nombre):
            trouve=True
        else:
            nombre+=1
    return nombre

def epreuve_math_premier():
    n=randint(10,20)
    print("Épreuve de Mathématiques: Trouver le nombre premier le plus proche de",n)
    nb_joueur=int(input("Saisir un nombre : "))
    if premier_plus_proche(n)==nb_joueur:
        return True
    else:
        return False

#epreuve 3, la roulette
def epreuve_roulette_mathematique():
    liste_nb=[]
    somme=0
    for i in range(5):
        liste_nb.append(randint(1,20))
    operation=randint(1,3)
    print(liste_nb[:])
    if operation==1:
        for i in range(5):
            somme+=liste_nb[i]
        print("Calculez le résultat en combinant ces nombres avec une addition")
    elif operation==2:
        for i in range(5):
            somme= somme-liste_nb[i]
        print("Calculez le résultat en combinant ces nombres avec une soustraction")
    else:
        for i in range(5):
            somme = somme * liste_nb[i]
        print("Calculez le résultat en combinant ces nombres avec une mulitplication")
    reponse=int(input("Votre réponse : "))
    if reponse==somme:
        return True
    else:
        return False


#epreuve générale de maths
def epreuve_math()->bool:
    epreuve=[epreuve_factorielle,epreuve_math_premier,epreuve_roulette_mathematique]
    aleatoire=randint(0,2)
    epreuve=epreuve[aleatoire]
    return epreuve()
print(epreuve_math())