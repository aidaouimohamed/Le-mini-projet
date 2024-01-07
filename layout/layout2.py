from dash import html, dcc

def create_layout(app):
    # Create a container for the entire layout of the web page
    return html.Div([
        # Header with the title, centered on the page
        html.H1("Nombre d'alternant par niveau d'étude pour chaque année", style={'textAlign': 'center'}),

        # Container for the year selection dropdown
        html.Div([
            # Label for the dropdown
            html.Label("Sélectionnez une année :"),

            # Dropdown for selecting a year
            dcc.Dropdown(
                id='annee-selector',  # Unique identifier for the dropdown
                # Options for the dropdown are years, taken from app configuration
                options=[{'label': annee, 'value': annee} for annee in app.server.config['annees']],
                value=app.server.config['annees'][0],  # Default value is the first year in the list
                clearable=False  # User cannot clear the selection, a value must be chosen
            ),
        ], style={'width': '20%', 'margin': '0 auto'}),  # Style to center the dropdown

        # Placeholder for the graph which will be rendered here
        dcc.Graph(id='graphique-alternance')
    ], style={'padding': 50})  # Padding around the entire layout
