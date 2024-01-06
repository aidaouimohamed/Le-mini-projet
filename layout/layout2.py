from dash import html, dcc

def create_layout(app):
    return html.Div([
        html.H1("Statistiques des Alternances", style={'textAlign': 'center'}),
        html.Div([
            html.Label("Sélectionnez une année :"),
            dcc.Dropdown(
                id='annee-selector',
                options=[{'label': annee, 'value': annee} for annee in app.server.config['annees']],
                value=app.server.config['annees'][0],
                clearable=False
            ),
        ], style={'width': '48%', 'display': 'inline-block'}),
        dcc.Graph(id='graphique-alternance')
    ], style={'padding': 50})
