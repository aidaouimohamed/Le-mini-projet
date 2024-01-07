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



## Rapport d'Analyse des Données

### Vue d'ensemble

Le projet "Statistiques des Alternances" a pour but de fournir une analyse approfondie des offres d'alternance en France. Les données collectées proviennent de différentes sources et offrent un aperçu détaillé des tendances dans les offres d'emploi, les niveaux d'éducation requis, et la répartition géographique des alternances.

### Conclusions Principales

#### 1. Répartition Géographique des Offres d'Alternance
- **Constatation**: Une concentration élevée d'offres d'alternance dans les grands centres urbains, avec une présence significative dans des régions spécifiques.
- **Implication**: Nécessité de stratégies ciblées pour équilibrer les opportunités d'alternance à travers le pays.

#### 2. Tendances des Niveaux d'Éducation
- **Constatation**: La majorité des offres d'alternance requièrent un niveau d'éducation spécifique, souvent lié à des domaines techniques ou professionnels.
- **Implication**: Importance de l'adéquation entre les formations et les besoins du marché de l'emploi.

#### 3. Durée des Contrats d'Alternance
- **Constatation**: Une variété dans la durée des contrats, reflétant une flexibilité dans les parcours d'alternance.
- **Implication**: Opportunité pour les candidats de choisir des parcours adaptés à leurs besoins de carrière.

#### 4. Types de Contrats et Secteurs d'Activité
- **Constatation**: Une diversité dans les types de contrats et les secteurs, indiquant une large gamme d'opportunités disponibles.
- **Implication**: Nécessité pour les candidats de se renseigner sur les différents secteurs pour optimiser leurs choix de carrière.

### Méthodologie

Les données ont été extraites et traitées en utilisant des scripts Python, avec un focus particulier sur le nettoyage et la structuration des données pour l'analyse. Les analyses ont été réalisées à l'aide de visualisations interactives fournies par l'application Dash, permettant une exploration détaillée et personnalisée des données.

### Recommandations

- **Amélioration de l'Accès aux Informations**: Mettre en place des moyens pour faciliter l'accès aux informations sur les offres d'alternance, en particulier dans les régions moins desservies.
- **Adaptation des Programmes de Formation**: Aligner les programmes de formation sur les exigences du marché de l'emploi pour augmenter les chances d'employabilité des alternants.
- **Sensibilisation des Employeurs**: Encourager les employeurs à diversifier les offres d'alternance pour répondre à une gamme plus large de qualifications et d'intérêts.

### Conclusion

Ce projet met en évidence la dynamique du marché des alternances en France, offrant des perspectives précieuses et clairs pour les étudiants, et permet ainsi la visualisation et l'analyse de ces tendances, contribuant à une meilleure compréhension du paysage des alternances en France.
