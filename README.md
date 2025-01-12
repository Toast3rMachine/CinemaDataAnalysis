# CinemaDataAnalysis

## Sommaire
- [Réponses aux questions](https://github.com/Toast3rMachine/CinemaDataAnalysis?tab=readme-ov-file#r%C3%A9ponses-aux-questions)
- [Que fait ce projet ?](https://github.com/Toast3rMachine/CinemaDataAnalysis?tab=readme-ov-file#que-fait-ce-projet-)
- [Comment utiliser le projet ?](https://github.com/Toast3rMachine/CinemaDataAnalysis?tab=readme-ov-file#comment-utiliser-le-projet-)
- [Sources](https://github.com/Toast3rMachine/CinemaDataAnalysis?tab=readme-ov-file#sources)

## Réponses aux questions

### Exercice 3 - Question : Selon vous, quelle est la variable ayant le plus d’impact sur les entrées annuelles ?

Grâce aux tableaux de corrélation et aux grahiques, la variable qui semble avoir le plus d'impacts sur les entrées annuelles est celle des écrans. La corrélation Ecrans/Entrées est de 0.88 tandis que la corrélation Fauteuils/Entrées est de 0.84. La corrélation Ecrans/Entrées est donc plus forte que la seconde corrélation Fauteuils/Entrées.

### Exercice 4 - Question : Selon les performances du modèle, le nombre d’écrans ou de fauteuils est-il un bon prédicteur des entrées ?

Non. Les performances du modèle ne peuvent pas déterminées si le nombre d'écrans ou de fauteuils est un bon prédicteurs d'entrées car bien d'autres facteurs rentre en jeu, comme les films présenté durant l'année.
Bien sûr, mon modéle de prédiction peut très bien être totalement défectueux.

## Que fait ce projet ?

Ce projet est avant tout un projet d'école. 
Ce dernier consiste en la manipulation de données à partir d'un fichier csv dans le langage de programmation Python et en utilisant des librairies comme pandas, matplotlib et sklearn.
Ces librairies permettent la lecture et la manipulation de données à partir d'un fichier csv, la création de graphique et du machine learning afin de prédire des données.

Le fichier csv utilisé est un fichier regroupant les informations des cinémas présent en Ile-de-France.
Le fichier utilisé est trouvable en suivant ce lien : [salle_de_cinema_ile-de-france.csv](https://www.data.gouv.fr/en/datasets/etablissements-cinematographiques/)
Le nom de ce dernier a été modifié dans ce projet.

Le but de ce projet était de déterminée si les infrastuctures des salles de cinémas avaient un impact sur les entrées annuelles. En utilsant des graphes et un modèle de prédiction de données

## Comment utiliser le projet ?

### Initialisation du dossier venv

Ce projet Python nécessite un dossier local "venv".
Pour initialiser ce dossier, taper la commande suivante dans le terminal, à la racine du projet.

```
python3 -m venv venv
```

>[!WARNING]
>**Penser à configurer le terminal pour que ce dernier utilise le dossier venv présent dans le projet. Le dossier Python utiliser est visible en bas à droite de la fenêtre vscode. Si ("venv") n'est pas afficher, cliquer sur le dossier utiliser puis changer le pour le dossier ("venv") présent dans le projet. Le terminal devra être relancé.**

### Installation des librairies utilisées dans le projet

Ensuite, installer les différentes librairies requises au bon fonctionnement du projet.
Les librairies requises sont : pandas, matplotlib et sklearn.
Pour télécharger ces librairies, taper les commandes suivantes dans la console.

```
pip install pandas
pip install matplotlib
pip install scikit-learn
```

Après avoir effectué toutes ces étapes, vous devrez être en capacité de faire fonctionner le projet.

## Sources

Afin de réaliser ce projet, je me suis aidé de sites tels que :
- [StackOverflow](https://stackoverflow.com/)
- [La documentation de pandas](https://pandas.pydata.org/docs/)
- [La documentation de matplotlib](https://matplotlib.org/stable/index.html)
- [La documentation de sklearn](https://scikit-learn.org/stable/)
- [Datascientest](https://datascientest.com/regression-lineaire-tout-savoir) *Ressource sur la Régression Linéaire*

Ainsi que d'autres ressources trouvable sur Internet.
