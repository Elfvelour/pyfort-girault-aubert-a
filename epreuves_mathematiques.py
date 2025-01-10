##############################################
####### Programme Python epreuve maths #######
####### Auteur: Timothée Girault       #######
####### Version: 1.2                   #######
##############################################

##############################################
# Importation des fonctions externes

from  math import sqrt
from random import randint

##############################################
# Déclarations des fonctions utilisateurs

#  Epreuve 1 de maths, les factorielles: prend un nombre n en paramètre et renvoie sa factorielle
def factorielle(n):
    res=1
    if n==0:
        res=1
    else:
        #n!=n*(n-1)*(n-2)*....*2*1
        for i in range(n,1,-1):
            res=res*i
    return res

# Epreuve 1.1 de maths, le calcul de factorielles: demande au joueur de calculer la factorille
# d'un nombre n et renvoie vraie ou faux si la réponse du joueur est bonne ou non
def epreuve_factorielle():
    n=randint(1,10)
    res=factorielle(n)
    print("Épreuve de Mathématiques: Calculer la factorielle de ",n)
    resultat=(input("Votre réponse : "))
    if resultat==str(res):
        return True
    else:
        return False

# Epreuve 2, les nombres premiers: prend un nombre n et retourne s'il est premier par vraie ou faux
def est_premier(n):
    premier = True
    # boucle for  pour savoir s'il a plus de 2 diviseurs avec la méthode de la racine soit de 2 à
    # racine de n, qui permet de réduire énormement le nombre possible de diviseurs avec n
    for i in range(2, int(sqrt(n))+ 1):
        if n % i == 0:
            premier = False
    return premier

# Epreuve 2.1, le nombre premier le plus proche de n: prend en paramètre un nombre
# n et trouve le nombre premier le plus proche de n et le renvoie
def premier_plus_proche(n):
    trouve=False
    nombre=n
    #boucle while poour trouver le plus proche premier en appelant la fonction est_premier
    while not trouve:
        if est_premier(nombre):
            trouve=True
        else:
            nombre+=1
    return nombre

# Epreuve 2.2, le calcul du nombre premier le plus proche de n: demande au joueur de trouver le nombre premier
# le plus proche et renvoie par vraie ou faux s'il a une bonne réponse
def epreuve_math_premier():
    n=randint(10,20)
    print("Épreuve de Mathématiques: Trouver le nombre premier le plus proche de",n)
    nb_joueur=(input("Saisir un nombre : "))
    #compare la réponse du joueur et celle du programmme grâce à la fonction
    # premier_plus_proche et renvoie vraie ou faux
    if str(premier_plus_proche(n))==nb_joueur:
        return True
    else:
        return False

# Epreuve 3, la roulette mathématique : demande à l'utilisateur de calculer le résultat par addition, multiplication
# ou soustraction de 5 nombres et renvoie vrai ou faux si son résultat est bon ou pas
def epreuve_roulette_mathematique():
    liste_nb=[]
    resultat=0
    #choisi 5 nombres au hasard entre 1 et 20
    for i in range(5):
        liste_nb.append(randint(1,20))
    # choisi au hasard une des opérations +,- ou *
    operation=randint(1,3)
    print(liste_nb[:])
    #calcule pour l'opération choisi le résultat des 5 nombres et de demande à l'utilisteur sa réponse
    #et renvoie vraie ou faux s'il a bon ou pas
    if operation==1:
        for i in range(5):
            resultat+=liste_nb[i]
        print("Calculez le résultat en combinant ces nombres avec une addition")
    elif operation==2:
        for i in range(5):
            resultat= resultat-liste_nb[i]
        print("Calculez le résultat en combinant ces nombres avec une soustraction")
    else:
        resultat = 1
        for i in range(5):
            resultat = resultat * liste_nb[i]
        print("Calculez le résultat en combinant ces nombres avec une mulitplication")
    reponse=(input("Votre réponse : "))
    if reponse==str(resultat):
        return True
    else:
        return False

##############################################
# Corps du programme principal

# Epreuve générale de maths: chosi aléatoirement une des 3 épreuves parmi une liste et on lance cette épreuve
def epreuve_math()->bool:
    epreuve=[epreuve_factorielle,epreuve_math_premier,epreuve_roulette_mathematique]
    aleatoire=randint(0,2)
    epreuve=epreuve[aleatoire]
    return epreuve()
