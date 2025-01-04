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
- A la fin du fichier main.py : écrire jeu() et pour lancer le programme, appuyer sur le bouton vert 'run'. Le programme devrait gérer les erreurs.

- Pour les coordonnées du morpion. Il faut réfléchir en mode "Humain" et pas en mode "Python" pour ce qui est des indices. Par exemple la case tout en haut à gauche à pour coordonnées (1,1) et non (0,0).

- C'est la même chose pour le reste du projet.

- L'utilisation de majuscules ou de minuscules n'a pas d'impact dans la réponse du joueur

- Utilisation simple et instinctive.

    
# Documentation Technique
### Algorithme du jeu
1. On commence d'abord par importer les fonctions de chaques fichiers qui nous permettra de les utiliser dans le main.

2. Ensuite, on définie la fonction jeu():

3. On utilise les fonctions du fichier fonctions_utiles soit introduction() et composer_equipe() pour faire débuter la partie avec l'explication des règles et la création de l'équipe.

4. On définie la variable CLES_OBTENUES (pour compter les clés gagnés par les joueur) qui nous servira plus tard dans le programme.

5. La boucle while commence. Elle sert à faire continuer le jeu tant que le joueur n'a pas gagné 3 clés.

6. D'abord, on demande au joueur à quel jeu il souhaite jouer puis on demande de sélectionner un joueur de l'équipe qui réalisera l'épreuve.

7. Ensuite on effectue une série de test pour voir si l'épreuve que le joueur à sélectionné correspond à une des épreuves codés. Si c'est le cas, l'épreuve se lance et si le joueur réussi cette dernière, il gagne une clé. Alors la variable CLES_OBTENUES augmente de 1 et les clés rapporté par le joueur sélectionné au début de l'épreuve augmente de 1.

8. On répète cette action tant que le joueur n'a pas obtenu 3 clés.

9. Quand le joueur a obtenu les 3 clés. On lance la fonction codé dans le fichier epreuve_finale nommé salle_De_Tresor(). Si le joueur réussi cette dernière épreuve, il remporte la partie, sinon il perd.


### Details des fonctions implémentés
- 

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

- 22 décembre : fichier epreuve_finale fini. 

- Semaine du 23 décembre : fichier fonctions_utiles et main terminés sans trop de difficulté. Donc tous les fichiers du projet ont été aboutis.
 
- Semaine du 29 décembre: relecture de tous les fichiers, derniers tests et rédaction du fichier readme
### Répartition des tâches
- Chacun travaille dans les tâches qui lui ont été attribués. Puis on regarde le code du binôme pour s'assurer que tout est claire et que la consigne a bien été respecté.

- Timothée GIRAULT: epreuves_maths, epreuves_hasard, epreuve_finale et enigme_pere_fourras
  Chaque version du code '1.x' corespond au nombre x de vendredi passé sur le fichier.

- Thomas AUBERT : epreuve_logique, fonctions_utiles, main

- Tâche commune : faire le fichier README.md
# Tests et Validation
### Stratégie de Test
- On a testé chaque fonction principale de chaque fichier avant son utilisation dans le programme global (main.py)
  
- On teste chaque fonction après l'avoir codé en utilisant un print pour s'assurer qu'il renvoie bien ce qu'on voulait.
  
- Avant de commit on vérifie si tous les noms de variables sont claires, s'il n'y a pas de fautes d'orthographe ou de codes.
<p align="center">
<img src="C:\Users\girau\OneDrive\Images\Captures d’écran\anglaisslide"    width="350"/>
</p>
![Capture d'écran 2024-09-16 082541](https://github.com/user-attachments/assets/171f6354-6e73-4186-8014-36f0b36eca83)
