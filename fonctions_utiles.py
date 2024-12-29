##################################################################
####### Projet Fort Boyard                                      ##
####### Auteur : Thomas AUBERT                                  ##
####### est utile pour le main et le déroulement des épreuves   ##
##################################################################

#affiche le texte d'introduction. Ne renvoie rien car elle sert uniquement à l'affichage
def introduction():
    bienvenue = "Bonjour joueur ! Bienvenue dans Fort Pyard !"
    regle_intro = "Voici les règles du jeu :"
    regle = "Votre objectif est simple : Vous aller devoir accomplir des épreuves pour gagner des clés qui vous feront accéder à la salle du trésor !"
    regle_fin = "L'objectif est donc de ramasser trois clés pour accéder à la salle du trésor. Que python soit avec vous !"
    print("------------------------------------------------")
    print(bienvenue)
    print('------------------------------------------------')
    print(regle_intro)
    print(regle)
    print(regle_fin)
    print("------------------------------------------------")

#Permet de composer les équipes. La fonction renvoie une liste.
def composer_equipe():

    #Indiquer le nombre de joueur
    nb_joueur=int(input("Combien de joueurs voulez-vous dans votre équipe ? "))
    while nb_joueur>3 or nb_joueur<=0:
        print("La saisie n'est pas bonne veuillez réessayer :")
        nb_joueur=int(input())

    #ajoute les informations des joueurs
    joueurs = []
    for i in range(nb_joueur):
        dico_joueur={}
        dico_joueur['nom'] = input(f"Nom du joueur {i+1}: ")
        dico_joueur['profession'] = input(f"Profession du joueur {i+1}: ")
        dico_joueur["leader"] = input(f"Le joueur {i+1} est-il le leader de l'équipe ? Si oui entrez oui : ")
        dico_joueur["clés_gagnées"] = 0
        joueurs.append(dico_joueur)


    #test pour savoir s'il y a bien qu'un seul leader ou s'il y a un problème
    cpt=0
    for i in joueurs:
        for j in i.values():
            if j=='oui' or j=='Oui' or j=='OUI':
                cpt+=1

    #traite le problème s'il y a un problème de chef
    if cpt!=1: 
        print("Il y a un problème de chef dans cette équipe !")
        if cpt>1: #Dans ce cas il y a plus de 1 chef.
            print("Il y a plus de 1 chef dans cette équipe ! Veuillez entrer le bon chef !")
            nom_chef=input("Nom du chef : ")
            for i in range(len(joueurs)):
                if joueurs[i]['nom'] == nom_chef:
                    joueurs[i]['leader'] = "oui"
                else:
                    joueurs[i]['leader'] = "non"
        if cpt==0: #Ici aucun chef n'est présent.
            print("Vu que vous n'avez pas décidé de chef, le chef sera le joueur 1 !")
            joueurs[0]['leader'] = "oui"

    return joueurs

#Permet le choix des épreuves. Renvoie un entier.
def menu_epreuves():

    epreuves = ["épreuve de mathématiques" , "épreuve de logique", "épreuve du hasard", "énigme du père Fourras"]

    #affichage des épreuves proposées
    print("Voici le choix des épreuves :")
    for i in range(len(epreuves)):
        print(f"{i+1}. {epreuves[i]}")

    #Permet le choix des épreuves
    choix=int(input("Veuillez choisir une épreuve : "))-1
    while choix>3 or choix<0:
        print("Avez-vous peur de choisir votre épreuve ? Choisissez à nouveau l'épreuve : ")
        choix=int(input())-1

    return choix


#Permet de choisir un joueur dans une équipe. Prend en paramètre une liste qui correspond aux informations des joueurs d'une équipe
#La fonction renvoie un dictionnaire qui correspond au joueur sélectionné.
def choisir_joueur(equipe):

    #Permet l'affichage des membres de l'équipe
    nb_ligne = 1
    for k in equipe:
        ligne =f"{nb_ligne}. {k['nom']} ({k['profession']}) "
        if k['leader']=="oui":
            print(ligne + "- Leader")
        else:
            print(ligne + "- Membre")
        nb_ligne+=1

    #Permet le choix du joueur
    choix_joueur=int(input("Veuillez saisir le joueur qui doit jouer :"))-1
    while choix_joueur<0 or choix_joueur>2:
        print("Problème dans le choix du joueur. Veuillez réessayer :")
        choix_joueur=int(input())-1

    return equipe[choix_joueur]

#permet de mettre un mot en minuscule. Est utile dans d'autres fichiers. Renvoie une chaine de caractère
def mot_miniscule(mot):
    L = list(mot)
    mot_min = ''
    for i in range(len(L)):
        if ord(L[i]) > 62 and ord(L[i]) < 95:
            L[i] = chr(ord(L[i]) + 32)
    for i in range(len(L)):
        mot_min = mot_min + L[i]
    return mot_min



