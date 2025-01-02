#######################################
#### Projet Fort Boyard : Main     ####
#### Auteur : Thomas AUBERT        ####
#### Permet le déroulement du jeu  ####
#######################################

########################################################

#On importe toutes les fonctions de tous les fichiers
from epreuves_logique import *
from fonctions_utiles import *
from enigme_pere_fouras import *
from epreuve_finale import *
from epreuves_mathematiques import *
from epreuves_hasard import *

########################################################

#Début du programme.

#Fonction gérant le déroulement du jeu.
def jeu():

    #On commence par expliquer les règles puis par former l'équipe :)

    introduction()
    print("Commençons par former votre équipe (3 joueurs maximum):")
    equipe = composer_equipe()

    CLES_OBTENUES = 0
    #Boucle permettant le jeu.
    while CLES_OBTENUES != 3:

        choix_jeux = menu_epreuves() #On choisi quel jeu on souhaite jouer.
        choix_joueur = choisir_joueur(equipe) #Et quel joueur va jouer.

        #Les 4 tests si dessous permettent de jouer au jeu choisi.
        if choix_jeux == 0:                     #Il s'agit du jeu de maths
            if epreuve_math() == True:          #On fait jouer le joueur à une épreuve de maths
                choix_joueur["clés_gagnées"]+=1
                CLES_OBTENUES += 1
                print(f"Bravo {choix_joueur['nom']} ! Vous avez gagné une clé ! Vous avez",CLES_OBTENUES,"clé(s)\n")
            else:
                print("Dommage ! Vous avez perdu le jeu :/ \n")
        if choix_jeux == 1:                     #Il s'agit du jeu de logique (morpion)
            if jeu_tictactoe() == True:          #On Fait jouer le joueur au morpion
                choix_joueur["clés_gagnées"]+=1
                CLES_OBTENUES += 1
                print(f"Bravo {choix_joueur['nom']} ! Vous avez gagné une clé !  Vous avez",CLES_OBTENUES,"clé(s)\n")
            else:
                print("Dommage ! Vous avez perdu le jeu :/ \n")
        if choix_jeux == 2:                     #Il s'agit du jeu de hasard
            if epreuve_hasard() == True:        #on fait jouer le joueur au jeu de hasard
                choix_joueur["clés_gagnées"]+=1
                CLES_OBTENUES += 1
                print(f"Bravo {choix_joueur['nom']} ! Vous avez gagné une clé !  Vous avez",CLES_OBTENUES,"clé(s)\n")
            else:
                print("Dommage ! Vous avez perdu le jeu :/ \n")
        if choix_jeux == 3:                     #Il s'agit des énigmes du Père Fourras
            if enigmes_pere_fouras() == True:      #On fait jouer le joueur aux énigmes de Père Fourras
                choix_joueur["clés_gagnées"]+=1
                CLES_OBTENUES += 1
                print("Bravo ! Vous avez gagné une clé !  Vous avez",CLES_OBTENUES,"clé(s)\n")
            else:
                print("Dommage ! Vous avez perdu le jeu :/ \n")


    #Après avoir obtenu 3 clés. Le joueur accède à la salle du trésor !
    print("Passe-Partout et Passe-muraille vous félcite pour vos 3 clés. Voici votre clé géante :")
    print("------------------------------------------------ \n")
    print('''                    $$$$XXX$$$                                                                             
                  $$$&&$$$$&$$$$$$                                                                         
                $$&&$$$$XX   $$$$&$$                                                                       
               $$&&&$$$        $$$$$$                                                                      
              $$&&&$$          $&X&$$                                                                      
             $$&&&$$           $$$&$$$                                                                     
            $$$&&&$            $$X&$$$                                                                     
            $$&&&$$            $$$&&$                                                                      
           $$&&&&$           $$&$&$&$                                                                      
           $X&&$$           $$&x$$$$&&$$$$$$$                                                              
           $X$&$             $&$&$$$$$$$$&&$$$$&&$                                                         
           $$$&&            $$$&&&$&&&&$&$$$$$$&$&&$$                                                      
            $X$&$          $$$&&&$    $$&&&$$$$$$$$$&&&&$$$                                                
            $$X&$$        $$$&&$$       &&&&$&&$&$$$++xX$$$$$$$$$                                          
              $$$&$$  $$$$$&&&$$             $&&$$$&&&&$$X+xxX$$&&$$$$                                     
                &$$$$$$$$&&&$$                      X$$$$&&&$$XxxxX$$&$&$$$$                               
                   $$$$$$$$                              $$$$$$&$$$$XxxX$$$&&$$$$                          
                                                               X$$$$&&$$$XxxxX$$$&&$$$                     
                                                                     $$$$$&&$$$x+xX$$&&&$$$                
                                                                           $$$$&&$$$XXxX$$&&&&$$           
                                                                                 $$$&&&$$$XXX$$&$$&$$$     
                                                                                     $$$$$$&&$$XX$$$$$&&$  
                                                                                    $$$$$$$$$$$$$$$$$$$$$  
                                                                                    $$$$$$$$$$$$$&$$$$$$   
                                                                                   $$$$$$$$$$$$$$$         
                                                                                  $$$$$$$$$$$$$$$          
                                                                                 $$$$$$$$$$$$$$$           
                                                                                 $$$$$$$$$$$$$&$           
                                                                                  $$$$$$$$$$$$$            
                                                                                       $$$$$$$$            
                                                                                                           ''')
    print("------------------------------------------------")
    print("Vous entrez maintenant dans la salle du trésor ! \nUne dernière énigme vous sera posé. \nNe vous trompez pas sinon c'est perdu ! \n")
    if salle_DE_Tresor("./data/indicesSalle.json"): #Sert à faire commencer l'épreuve finale.
        print("Bravo vous avez volés nos boyards d'or")
    else:
        print("Nos boyards d'or sont à nous AH AH AH!")

print(jeu())