from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import json

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
                # Exclure les départements commençant par 97
                if code_dep.startswith('97'):
                    continue
                job['place']['code_departement'] = code_dep
                job['place']['departement'] = departements.get(code_dep, 'Inconnu')
                infos_departements.append(job['place'])

df = pd.DataFrame(infos_departements)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

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
                figure=px.scatter_mapbox(
                    df, lat='latitude', lon='longitude',
                    hover_name='departement', height=750,
                    color_discrete_sequence=["fuchsia"], zoom=5,
                    mapbox_style='carto-positron'
                )
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
        filtered_df = df[df['code_departement'] == selected_departement]

        # Vérification du nombre d'offres d'emploi filtrées
        print(f"Nombre d'offres d'emploi filtrées pour le département {selected_departement}: {len(filtered_df)}")

        # Calcul du centre géographique du département
        center_lat = filtered_df['latitude'].mean()
        center_lon = filtered_df['longitude'].mean()

        return px.scatter_mapbox(
            filtered_df, lat='latitude', lon='longitude',
            hover_name='departement', height=750,
            color_discrete_sequence=["fuchsia"],
            zoom=8,
            center={"lat": center_lat, "lon": center_lon},
            size_max=15,
            mapbox_style='carto-positron'
        )
    else:
        return px.scatter_mapbox(
            df, lat='latitude', lon='longitude',
            hover_name='departement', height=750,
            color_discrete_sequence=["fuchsia"], zoom=5,
            size_max=15,
            mapbox_style='carto-positron'
        )

if __name__ == '__main__':
    app.run_server(debug=True)
