from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import json
import numpy as np

# Fonction pour charger les départements
def charger_departements(fichier='departement.json'):
    with open(fichier, 'r') as file:
        data = json.load(file)
    return {dep['DEP']: dep['NCC'] for dep in data}

departements = charger_departements()

# Chargement des données d'emploi depuis un fichier JSON
with open('data.json', 'r') as file:
    responses = json.load(file)

infos_departements = []
for response in responses:
    if response and 'peJobs' in response and 'results' in response['peJobs']:
        for job in response['peJobs']['results']:
            if 'zipCode' in job['place']:
                code_dep = job['place']['zipCode'][:2]
                if code_dep.startswith('97'):
                    continue
                job['place']['code_departement'] = code_dep
                job['place']['departement'] = departements.get(code_dep, 'Inconnu')
                job['place']['intitule_poste'] = job['title'] if 'title' in job else 'Inconnu'
                job['place']['type_contrat'] = job['job']['contractType'] if 'job' in job and 'contractType' in job['job'] else 'Inconnu'
                infos_departements.append(job['place'])

df = pd.DataFrame(infos_departements)

# ... reste du code ...


# Ajout d'un identifiant unique pour chaque point
df['unique_id'] = df.index

# Fonction pour ajouter un léger décalage aléatoire aux coordonnées
def ajouter_decalage(df, colonnes=['latitude', 'longitude'], decalage_max=0.009):
    for col in colonnes:
        df[col] = df[col].apply(lambda x: x + np.random.uniform(-decalage_max, decalage_max))
    return df

# Appliquez cette fonction au DataFrame
df = ajouter_decalage(df)

# Palette de couleurs personnalisée avec des tons plus foncés
couleurs_personnalisees = ['#003f5c', '#2f4b7c', '#665191', '#a05195', '#d45087', '#f95d6a', '#ff7c43', '#ffa600']

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Fonction pour créer la carte avec des couleurs personnalisées pour chaque point
def create_map(dataframe):
    return px.scatter_mapbox(
        dataframe, lat='latitude', lon='longitude',
        hover_name='departement',
        hover_data={'intitule_poste': True, 'type_contrat': True, 'latitude': False, 'longitude': False, 'unique_id': False},
        height=750,
        color='unique_id',
        color_continuous_scale=couleurs_personnalisees,
        zoom=5,
        mapbox_style='carto-positron'
    )

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='departement-dropdown',
                options=[{'label': name, 'value': code} for code, name in departements.items()],
                value=None,
                placeholder="Sélectionnez un département"
            )
        ], width=4),
        dbc.Col([
            dcc.Markdown('# Carte des Offres d\'Emploi par Département', style={'textAlign': 'center'})
        ], width=8)
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='job-map',
                figure=create_map(df)
            )
        ], width=12)
    ])
])

@app.callback(
    Output('job-map', 'figure'),
    [Input('departement-dropdown', 'value')]
)
def update_map(selected_departement):
    if selected_departement is not None:
        filtered_df = df[df['code_departement'] == selected_departement].copy()
        filtered_df = ajouter_decalage(filtered_df)

        center_lat = filtered_df['latitude'].mean()
        center_lon = filtered_df['longitude'].mean()

        return px.scatter_mapbox(
            filtered_df, lat='latitude', lon='longitude',
            hover_name='departement',
            hover_data={'intitule_poste': True, 'type_contrat': True, 'latitude': False, 'longitude': False, 'unique_id': False},
            height=750,
            color='unique_id',
            color_continuous_scale=couleurs_personnalisees,
            zoom=10,
            center={"lat": center_lat, "lon": center_lon},
            mapbox_style='carto-positron'
        )
    else:
        return create_map(df)

if __name__ == '__main__':
    app.run_server(debug=True)
