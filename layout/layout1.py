from dash import html, dcc

def create_layout():
    return html.Div([
        # Title of the dashboard, centered
        html.H1("Dashboard des Offres d'Emploi par Département", style={'textAlign': 'center'}),
        
        # Container for the slider and its label
        html.Div([
            # Label for the slider
            html.Label("Afficher uniquement les départements ayant un nombre d'offres supérieur ou égal à la valeur choisie : ", style={'display': 'flex', 'justifyContent': 'center'}),
            
            # Slider component for selecting the minimum number of job offers
            html.Div(
                dcc.Slider(
                    id='min-offre-slider',
                    min=0,  # Minimum value of the slider
                    max=100,  # Maximum value of the slider (adjustable based on data)
                    value=5,  # Initial value of the slider
                    marks={i: str(i) for i in range(0, 101, 5)},  # Marks on the slider at intervals of 5
                    step=1  # Step size of the slider
                ),
                style={'width': '70%', 'margin': 'auto'}  # Styling for the slider container
            )
        ], style={'padding': '20px', 'margin': '20px'}),  # Styling for the outer container of the slider

        # Container for the graph that will be updated based on the slider value
        html.Div(id='graph-container', style={'display': 'flex', 'justifyContent': 'center'})
    ])
