from dash import dcc, html
import dash_bootstrap_components as dbc
from data_processing import charger_departements, load_data
from graphs import create_map

departements = charger_departements()
df = load_data()

def create_layout():
    return dbc.Container([
        # Row for the title
        dbc.Row([
            dbc.Col([
                dcc.Markdown('# Carte des Offres d\'alternance en France', style={'textAlign': 'center'})
            ], width=12)
        ]),
        # Row for department selection (centered with spacers)
        dbc.Row([
            # Left spacer
            dbc.Col(width=4),
            # Dropdown
            dbc.Col([
                dcc.Dropdown(
                    id='departement-dropdown',
                    options=[{'label': name, 'value': code} for code, name in departements.items()],
                    value=None,
                    placeholder="Sélectionnez un département"
                )
            ], width=4),
            # Right spacer
            dbc.Col(width=4),
        ]),
        # Row for the graph
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    id='job-map',
                    figure=create_map(df)
                )
            ], width=12)
        ])
    ])

