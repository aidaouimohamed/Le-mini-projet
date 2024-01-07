# Import necessary libraries
from dash import dcc, html
import dash_bootstrap_components as dbc
from data_processing import charger_departements, load_data
from graphs import create_map

# Load department data and dataset
departements = charger_departements()
df = load_data()

# Function to create the layout of the dashboard
def create_layout():
    return dbc.Container([
        # Row for the title of the dashboard
        dbc.Row([
            dbc.Col([
                dcc.Markdown('# Carte des Offres d\'alternance en France', style={'textAlign': 'center'})
            ], width=12)
        ]),
        # Row for selecting a department with space on both sides for centering
        dbc.Row([
            # Left spacer for centering the dropdown
            dbc.Col(width=4),
            # Dropdown for selecting a department
            dbc.Col([
                dcc.Dropdown(
                    id='departement-dropdown',
                    options=[{'label': name, 'value': code} for code, name in departements.items()],
                    value=None,
                    placeholder="Sélectionnez un département"
                )
            ], width=4),
            # Right spacer for centering the dropdown
            dbc.Col(width=4),
        ]),
        # Row for displaying the map graph
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    id='job-map',
                    figure=create_map(df)
                )
            ], width=12)
        ])
    ])
