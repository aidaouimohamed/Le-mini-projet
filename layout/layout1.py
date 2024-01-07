from dash import html, dcc

def create_layout():
    return html.Div([
        html.H1("Dashboard des Offres d'Emploi par Département", style={'textAlign': 'center'}),
        html.Div([
            html.Label("Afficher uniquement les départements ayant un nombre d'offres supérieur ou égal à la valeur choisie : ", style={'display': 'flex', 'justifyContent': 'center'}),
            html.Div(
                dcc.Slider(
                    id='min-offre-slider',
                    min=0,
                    max=100,  # Adjust max based on your data
                    value=5,
                    marks={i: str(i) for i in range(0, 101, 5)},
                    step=1
                ),
                style={'width': '70%', 'margin': 'auto'}
            )
        ], style={'padding': '20px', 'margin': '20px'}),
        html.Div(id='graph-container', style={'display': 'flex', 'justifyContent': 'center'})
    ])
