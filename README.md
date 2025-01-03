# Projet Python : Fort Boyard
### Contributeurs:
#### -Thomas Aubert
rôle: codage des fonctions utiles, logiques et main
#### -Timothée Girault:
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
### Details des fonctions implémentés
### Gestion des Entrées et Erreurs
- Utilisations de boucle while (qui redemande au joueur de soumettre sa réponse) si la réponse du joueur n'est pas dans la sélection des réponses attendus comme A,B ou C dans le jeu du bonneteau
- Mettre la réponse soit totalement en majuscule ou en minuscule (pour savoir si la réponse est bonne ou non) pour éviter d'avoir la bonne réponse en majuscule, dans la liste en minuscule et de renvoyer une mauvaise réponse.
#### Liste des bugs:
- list out of range
- variable is no defined
- expected an indented block
- [Errno 2] No such file or directory
# Journal de bord
### Chronologie du Projet:
- Semaine du 9 décembre : Début du projet avec le début du morpion, le fichier epreuves_maths et epreuve_hasard commencés.

- Semaine du 16 décembre : Morpion terminé, fichier epreuve_hasard, epreuve_maths, enigme_pere_fourras et epreuve_finale terminés.

- Semaine du 23 décembre : fichier fonctions_utiles et main terminés. Donc tous les fichiers du projet ont été aboutis.
 
- Semaine du 29 décembre: relecture de tous les fichiers, derniers tests et rédaction du fichier readme
### Répartition des tâches
- Timothée GIRAULT: epreuves_maths, epreuves_hasard, epreuve_finale et enigme_pere_fourras

- Thomas AUBERT : epreuve_logique, fonctions_utiles, main

- Tâche commune : faire le fichier README.md
# Tests et Validation
### Stratégie de Test
- On a testé chaque fonction principale de chaque fichier avant son utilisation dans le programme global (main.py)
  
- On teste chaque fonction après l'avoir codé en utilisant un print pour s'assurer qu'il renvoie bien ce qu'on voulait.
  
- Avant de commit on vérifie si tous les noms de variables sont claires, s'il n'y a pas de fautes d'orthographe ou de codes.
