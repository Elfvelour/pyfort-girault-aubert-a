# Projet Python : Fort Boyard
### Contributeurs:
#### -Thomas Aubert
rôle: codage des fonctions utiles, logiques et main
#### -Timothée Girault
rôle: codage des fonctions finales, mathématiques, hasard et Père Fouras
### Description
Création du jeux mythique Fort Boyard en Python. Le ou les joueur(s) doivent rassembler 3 clés au travers de 4 thèmes:

-Les épreuves de logiques

-Les épreuves de mathématiques

-Les épreuves de hasards

-Les énigmes du Père Fouras

Puis de gagner les boyards d'or en trouvant le mot secret dans l'épreuve finale

### Fonctionalités principales du projet
- Coordination de plusieurs fichiers

- Utilisation de fichiers json

- Création d'un jeu interactif

### Technologies Utilisées
- Langage python	

- Pycharm

- Fichiers json pour les énigmes du Père Fouras et l'épreuve finale

- Bibliothèque random	

- Bibliothèque math

### Installation

#### Instruction pour clôner le dépôt Github:
1.Tout d'abord, vérifier d'avoir créer le projet en privé et ajouter le binôme ainsi que les professeurs dans les collaborateurs.

2.Ouvrir le projet puis aller dans code, cliquer sur le bouton vert 'code' et copier le lien https

3.Créer un fichier et l'ouvrir sur Pycharm

4.Aller dans le terminal et écrire 'git clone'avec le lien https

5.S'identifier à Github pour clôner le dépôt avec la clé à 6 chiffres et commencer à coder

#### Configuration de l'environnement de développement:
- Installation de l'application Pycharm sur notre PC en récupérant notre licence étudiante sur le site JetBrains²

- Création d'un compte Github avec l'email de l'EFREI

- Création d'un projet sur Github en ajoutant le binôme et les profeseurs en tant que collabarateurs

- Premier "commit" de tous les fichiers pour initialiser le projet et commencer à développer

### Utilisation
- A la fin du fichier *__main.py__* : écrire jeu() et pour lancer le programme, appuyer sur le bouton vert 'run'. Le programme devrait gérer les erreurs.

- Pour les coordonnées du morpion. Il faut réfléchir en mode "Humain" et pas en mode "Python" pour ce qui est des indices. Par exemple la case tout en haut à gauche à pour coordonnées (1,1) et non (0,0).

- C'est la même chose pour le reste du projet.

- L'utilisation de majuscules ou de minuscules n'a pas d'impact dans la réponse du joueur

- Utilisation simple et instinctive.

    
# Documentation Technique
### Algorithme du jeu
1. On commence d'abord par importer les fonctions de chaques fichiers qui nous permettra de les utiliser dans le main.

2. Ensuite, on définie la fonction *__jeu()__*:

3. On utilise les fonctions du fichier fonctions_utiles soit *__introduction()__* et *__composer_equipe()__* pour faire débuter la partie avec l'explication des règles et la création de l'équipe.

4. On définie la variable __CLES_OBTENUES__ (pour compter les clés gagnés par les joueur) qui nous servira plus tard dans le programme.

5. La boucle while commence. Elle sert à faire continuer le jeu tant que le joueur n'a pas gagné 3 clés.

6. D'abord, on demande au joueur à quel jeu il souhaite jouer puis on demande de sélectionner un joueur de l'équipe qui réalisera l'épreuve.

7. Ensuite on effectue une série de test pour voir si l'épreuve que le joueur à sélectionné correspond à une des épreuves codés. Si c'est le cas, l'épreuve se lance et si le joueur réussi cette dernière, il gagne une clé. Alors la variable **CLES_OBTENUES** augmente de 1 et les clés rapporté par le joueur sélectionné au début de l'épreuve augmente de 1.

8. On répète cette action tant que le joueur n'a pas obtenu 3 clés.

9. Quand le joueur a obtenu les 3 clés. On lance la fonction codé dans le fichier epreuve_finale nommé *__salle_De_Tresor()__*. Si le joueur réussi cette dernière épreuve, il remporte la partie, sinon il perd.


### Details des fonctions implémentés
 Fonctions de la partie de Thomas :
 
 #### fonction *afficher(grille):*
 - Prend en paramètre un tableau et qui renvoie un tableau. Elle sert uniquement d'affichage.
 - 
 #### Fonction *est_entree_valide(entree):*
 - elle renvoie True si les coordonnées saisies par le joueur sont valides. Elle renvoie False sinon.

 #### fonction *tour_joueur(grille):*
 - Elle permet de saisir le coup du joueur. Elle ne renvoie rien.

 #### fonction *verifier_victoire(grille,symbole):*
 - Elle prend en paramètre la grille de jeu et le symbole que le souhaite verifier si il y a victoire. Elle renvoie True s'il y a victoire. Renvoie False sinon.

 #### fonction *grille_complete(grille):*
 - Elle prend en paramètre la grille de jeu. Elle renvoie True si toutes les cases sont remplies. Renvoie False sinon.

 #### fonction *verifier_resultat(grille):*
 - La  permet juste de verifier s'il y a une victoire (et de qui ?) ou un match nul. Elle renvoie qui à gagné ou s'il y a match nul

 #### fonction *coup_maitre(grille, symbole):*
 - Elle prend en paramètre la grille de jeu et permet de connaitre le meilleur coup à jouer pour le maitre selon des règles précises. Elle renvoie un tuple qui correspond aux coordonnées du coup à jouer.

 #### fonction *tour_maitre(grille):*
 - Elle permet de faire jouer le maitre.

 #### fonction *jeu_tictactoe():*
 - Elle permet simplement le déroulement de la partie.

 #### fonction *introduction():*
 - Elle premet l'affichage des règles du jeu.

 #### fonction *composer_equipe():*
 - Elle permet de composer les équipes. Elle renvoie une liste de dictionnaires.

 #### *fonction menu_epreuve():*
 - Elle permet la sélection de l'épreuve. Elle renvoie le choix du joueur (int).

 #### fonction *choisir_joueur():*
 - la  permet d'afficher les joueurs de l'équipe puis de demander de sélectionner le joueur qui réalisera l'épreuve. Elle renvoie un dictionnaire.

 #### fonction *mot_minuscule(mot):*
 - Elle permet de rendre une chaine de caracère en majuscule en minuscule.

 #### fonction *jeu():*
 - Elle correspond à la fonction principale du jeu. Elle s'occupe du déroulé du jeu. Donc la fonction ne renvoie rien.


### Epreuves de mathématiques:
#### Fonction *factorielle(n)*
Cette fonction calcule la factorielle d'un entier n qui est en paramètre
#### Fonction *epreuve_factorielle()*
C'est la première épreuve du module des épreuves mathématiques, qui choisi un nombre n entre 1 et 10 et calculant sa factorielle. Elle fait appel à la fonction *__factorielle()__*
#### Fonction *est_premier(n)*
Cette fonction est utilisée pour savoir si le nombre entier n en paeamètre est premier ou non
#### Fonction *premier_plus_proche(n)*
Cette fonction est utilisée pour déterminer qui est le nombre premier le plus proche du nombre entier n en paramètre. Elle fait appel à la fonction *__est_premier__*
#### Fonction *epreuve_math_premier()*
C'est la deuxième épreuve du module, qui choisi aléatoirement un entier n entre 10 et 20 et déterminant le nombre premier le plus proche de n. Elle fait appel à la fonction *__premier_plus_proche__*
#### Fonction *epreuve_roulette_mathematique()*
C'est la troisième épreuve du module, qui choisi au hasard soit une multiplication, addition ou soustravtion de tout les nombres (5 nombres générés aléatoirement).
#### Fonction *epreuve_math()*
Cette fonction prend au hasard une des 3 épreuves et lance le jeu de cette dernière.
Elle fait appel aux fonctions *__epreuve_roulette_mathematique()__*,*__epreuve_math_premier()__* et *__epreuve_factorielle()__*

### Epreuves de hasard:
#### Fonction *bonneteau()*
C'est la première épreuve du module ds épreuves de hasard, qui choisi aléatoirment où la clé est caché parmi 3 verres: A, B ou C. On a 2 tentatives pour la trouver
#### Fonction  *lance_de_des()*
#### Fonction  *epreuve_hasard()*
Cette fonction choisi au hasard l'une des 2 épreuves du module et la renvoie. Elle fait appel aux
fonctions *__lance_de_des()__* et *__bonneteau()__*.
### Epreuves de logiques
### Epreuve finale:
### Fonctions utiles:
### Enigme Père Fouras:



#### Gestion des Entrées et Erreurs : 
- Pour les entrées, des saisies sécurisées sont proposées. On peut prendre l'exemple de l'utilisations de boucles while, si la réponse du joueur n'est pas dans la sélection des réponses attendus ( soit A,B ou C dans le jeu du bonneteau), la boucle redemande au joueur de soumettre sa réponse.
- Plusieurs tests ont été effectués avec des erreurs comises volontairement. Le programme arrive à fonctionner sans trop de problèmes. Par exemple, si on nomme 2 chefs dans une équipe, le programme le détecte et demande de saisir le bon chef. Dans le morpion, la saisie est complètement sécurisé (tout types d'erreurs ont été comises et le programme redemande la saisie des coordonnés).
- Mettre la réponse soit totalement en majuscule ou en minuscule (pour savoir si la réponse est bonne ou non) pour éviter d'avoir la bonne réponse en majuscule, dans la liste en minuscule et de renvoyer une mauvaise réponse.
#### Liste des bugs connus:
- Lorsque qu'on demande la saisie d'un entier (int), si on met un caractère (str) à la place, le programme plante

- L'oubli de définir une variable: 'variable is not defined'

- Un intervalle qui met 'out of range' la liste

- Le fichier qui n'est pas trouvé avec l'erreur '[Errno 2] No such file or directory'
# Journal de bord
### Chronologie du Projet:
- 6 décembre : Début du projet avec la création de tous les fichiers '.py', début du morpion, le fichier epreuves_mathématiques fini et epreuves_hasard commencés. Petit problème concernant la création de la fonction 'epreuve' (dans epreuves_mathématiques) par rapport à la liste qui permet de choisir aléatoirement l'épreuve.C'était comment écrire les épreuves dans la liste. J'ai résolu le problème à l'aide d'un camarade de classe qui m'a aidé.

- 13 décembre: fichier epreuve_hasard fini. Problème d'affichage pour écrire les règles du bonneteau, avec plusieurs lignes sans espaces entre chaque ligne. J'ai mis un petit peu de temps avant de réaliser qu'il fallait juste mettre un '\n' quand on voulait retourner à la ligne. Décision finale de partage des tâches: Thomas code le main, les fonctions utiles et le morpion et moi le reste car il met beaucoup de temps à finir le morpion, j'avance beaucoup plus vite que lui et pour respecter le partage égal des tâches

- 20 décembre : Morpion terminé, correction mineur du fichier epreuves_mathématiques pour la fonction est_premier, début du codage de l'épreuve finale et finalisation des énigmes du Père Fouras. Problème majeur qui m'aura pris beaucoup de temps (des 3h de projet le vendredi) sur le fichier enigme_pere_fouras pour mettre le fichier json dans le bon dossier du projet, taper le bon chemin vers ce fichier afin que la fonction marche sans erreur. J'ai résolu ce problème grâce à un camarade et le professeur Monsieur Elloumi. Ajout égalemment de phrases du Père Fouras (pour mettre un peu d'originalité dans le code) dans le code pour féliciter ou taquiner les joueurs.

- 22 décembre : fichier epreuve_finale fini. J'ai eu du mal pour chosir au hasard l'émission de l'épreuve finale en sélectionnant le bon chemin pour avoir les indices et le mot code dans ce dictionnaire de dictionnaire de dictionnaire (fichier enigmesPF.json). Il fallait choisir l'année puis l'émission et enfin afficher les 3 premiers indices. J'ai réussi grâce à l'aide de Mr Elleoumi.

- Semaine du 23 décembre : fichier fonctions_utiles et main terminés sans trop de difficulté. Donc tous les fichiers du projet ont été aboutis. Avancement des commentaires et de la mise en forme des fichiers.
 
- 30 décembre: relecture de tous les fichiers, derniers tests et rédaction du fichier readme.
  
- 3 janvier: avancement du fichier readme,ajout de 2 images en ASCII pour mettre un peu d'origianlité, changements mineur dans les commentaires.



Journal de Thomas :
- 6 Décembre, début du projet : J'ai directement voulu commencer par le morpion car j'avais déjà réalisé le code auparavant mais à 2 joueurs. J'ai donc voulu commencé par ça car ça me semblait plus simple. Il me suffisait d'ajuster mon programme déjà existant. Mais j'ai eu beaucoup de mal à comprendre pourquoi il fallait faire autant de fonctions dans le projet.

- 13 Décembre : Toujours beaucoup de mal à ajuster le programme initiale alors j'ai pris la décision de recommencer de 0 pour partir sur "de bonnes bases". J'ai codé l'affichage du morpion, la verification de victoire, la saisie des coordonnées du joueur, la partie du maitre (qui ne marchait pas) et la boucle pour faire tourner le jeu.

- 20 Décembre : Avec l'aide d'un camarde, j'ai recommencé de 0 la partie de Maitre car je n'arrivais plus à comprendre ce que j'avais fait la séance précédente. Au final, après 2 bonnes heures, j'ai réussi et terminé le morpion. Puis j'ai commencé la partie **fonction_utile.py**.

- Première semaine des vacances : J'ai terminé la partie **fonction_utile.py** sans trop de problèmes en 1h30. Puis dans la foulée le **main.py** toujours sans trop de soucis.

- Deuxième semaine de vacances : Je me suis occupé de mes parties sur le README.md 



- 1ère utilistaion pour nous deux de Github donc des commit pas tout le temps pertinant, les noms de commit pas assez claire et une inégalité des commit entre nous deux. Nos commit seront mieux gérés dans le futur. Nous nous excusons pour cette illisibilité.
### Répartition des tâches
- Chacun travaille dans les tâches qui lui ont été attribués. Puis on regarde le code du binôme pour s'assurer que tout est claire et que la consigne a bien été respecté.

- Timothée GIRAULT: epreuves_maths, epreuves_hasard, epreuve_finale et enigme_pere_fourras
  Chaque version du code '1.x' corespond au nombre x de vendredi passé sur le fichier.

- Thomas AUBERT : epreuve_logique, fonctions_utiles, main

- Tâche commune : faire le fichier README.md
# Tests et Validation
### Stratégie de Test
- On a testé chaque fonction principale de chaque fichier avant son utilisation dans le programme global (*__main.py__*)
  
- On teste chaque fonction après l'avoir codé en utilisant un print pour s'assurer qu'il renvoie bien ce qu'on voulait.
  
- Avant de commit on vérifie si tous les noms de variables sont claires, s'il n'y a pas de fautes d'orthographe ou de codes.


Test des erreurs sur le morpion.
<p align="left">
<img src="screenshot test projet/image5.png"    width="350"  />
</p>


Test sur le nombre de joueurs dans une équipe (fonction *composer_equipe():*)
<p align="left">
<img src="screenshot test projet/image4.png"    width="350"/>
</p>


Test sur la saisie des joueurs des équipes. Plus précisément si il y a 2 chefs (ou plus) dans une même équipe.
<p align="left">
<img src="screenshot test projet/image3.png"    width="350"/>
</p>


Test sur le choix des épreuves.
<p align="left">
<img src="screenshot test projet/image2.png"    width="350"/>
</p>



Test sur la saisie du joueur qui doit réaliser l'épreuve.
<p align="left">
<img src="screenshot test projet/image1.png"    width="350"/>
</p>


