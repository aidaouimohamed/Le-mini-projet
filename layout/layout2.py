from dash import html, dcc

def create_layout(app):
    return html.Div([
        html.H1("Nombre d'alternant par niveau d'étude pour chaque année", style={'textAlign': 'center'}),
        html.Div([
            html.Label("Sélectionnez une année :"),
            dcc.Dropdown(
                id='annee-selector',
                options=[{'label': annee, 'value': annee} for annee in app.server.config['annees']],
                value=app.server.config['annees'][0],
                clearable=False
            ),
        ], style={'width': '20%', 'margin': '0 auto'}),  # Modification ici pour centrer
        dcc.Graph(id='graphique-alternance')
    ], style={'padding': 50})
