from dash import dcc, html
import dash_bootstrap_components as dbc
from data_processing import charger_departements, load_data
from graphs import create_map

departements = charger_departements()
df = load_data()

def create_layout():
    return dbc.Container([
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
