# Le-mini-projet PYTHON


# les membres du projet :  
- Hocine BOUROUIH     
- AIDAOUI Mohamed    


# lien dépôt Git :
https://github.com/aidaouimohamed/Le-mini-projet.git   


# Guide Utilisateur
Pour utiliser l'application : 
1. Cloner le projet avec `git clone https://github.com/aidaouimohamed/Le-mini-projet.git`
2. Récupérer les données avec `python get_data.py`
3. Lancez l'application avec `python app.py`
4. Ouvrez un navigateur et accédez à `localhost:8050`.
5. Interagissez avec les différents éléments de l'interface, tels que les sliders, les cartes et les graphiques.


### Configuration Environnement

1. Installez les dépendances : `pip install -r requirements.txt`.
2. Exécutez `app.py` pour démarrer le serveur Dash.


# Statistiques des Alternances

## Introduction

Ce projet Dash fournit une application web interactive pour visualiser les statistiques des offres d'alternance en France. Il utilise Dash avec Bootstrap pour le frontend et pandas pour le traitement des données.
le producteur de données : data.gouv.fr

## Principales Conclusions

- Visualisation des offres d'alternance par département, niveau d'étude, et durée.
- Filtrage dynamique des données en fonction des critères sélectionnés par l'utilisateur.
- Cartographie des offres d'alternance sur une carte interactive.

## Données Utilisées

Les données utilisées dans ce projet proviennent de data.gouv.fr, elle sont télécharger et stocker en local la commande `python get_data.py` fait ça automatiquement. Elles incluent des informations sur les offres d'emploi, les niveaux de diplôme, et les caractéristiques géographiques des alternances.


## Guide Développeur

### Structure du Projet

- `app.py` : Point d'entrée principal de l'application Dash.
- `data_processing` : Contient les scripts pour le traitement des données.
- `layout` : Dossiers contenant les fichiers de mise en page de l'application.
- `callbacks` : Gère les interactions et les callbacks de Dash.
- `graphs` : Scripts pour la création de graphiques Plotly.


## Architecture du Projet

L'application utilise une architecture modulaire, séparant la logique de traitement des données, la gestion des callbacks, et la présentation. Cela permet une meilleure organisation du code et facilite la maintenance.
