import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import requests
import plotly.graph_objs as go

# Fonction pour récupérer les dimensions depuis l'API
def get_dimensions(api_url):
    response = requests.get(api_url)
    response.raise_for_status()  # Lève une exception pour les codes HTTP d'erreur
    data = response.json()
    return data['value']





# Fonction pour récupérer les données pour une dimension donnée
def get_data_for_dimension(api_url, dimension_code):
    response = requests.get(f"{api_url}/{dimension_code}")
    response.raise_for_status()
    data = response.json()

    # Inspectez la structure réelle des données pour déterminer la bonne clé
    if 'value' in data:
        return data['value']
    else:
        # Ajoutez une gestion d'erreur appropriée si la clé attendue n'est pas trouvée
        print(f"La clé 'value' n'a pas été trouvée dans les données pour la dimension {dimension_code}.")
        return []





# Configuration de l'application Dash
app = dash.Dash(__name__)




# URL de l'API
api_url = "https://ghoapi.azureedge.net/api/Dimension"
dimensions = get_dimensions(api_url)





# Mise en page du dashboard
app.layout = html.Div([
    html.H1("WHO API Dashboard"),
    
    html.Label("Sélectionnez une dimension :"),
    dcc.Dropdown(
        id='dimension-dropdown',
        options=[{'label': dimension['Title'], 'value': dimension['Code']} for dimension in dimensions],
        value=dimensions[0]['Code']
    ),
    
    dcc.Graph(id='dimension-graph'),

    html.Div(id='selected-dimension'),
])





# Callback pour mettre à jour l'affichage en fonction de la dimension sélectionnée
@app.callback(
    [Output('selected-dimension', 'children'),
     Output('dimension-graph', 'figure')],
    [Input('dimension-dropdown', 'value')]
)
def update_selected_dimension(selected_dimension):
    data = get_data_for_dimension(api_url, selected_dimension)

    # Ajoutez une impression pour déboguer
    print(f"Data for dimension {selected_dimension}: {data}")

    # Assurez-vous que les noms de clés correspondent à la structure réelle des données
    x_data = [entry.get('Year', 0) for entry in data]
    y_data = [entry.get('Value', 0) for entry in data]

    # Ajoutez une impression pour déboguer
    print(f"x_data: {x_data}")
    print(f"y_data: {y_data}")

    # Création de la trace de la courbe
    trace = go.Scatter(
        x=x_data,
        y=y_data,
        mode='lines+markers',
        name='Courbe de la dimension'
    )

    layout = go.Layout(
        title=f"Courbe de la dimension {selected_dimension}",
        xaxis=dict(title='Année'),
        yaxis=dict(title='Valeur')
    )

    return f"Vous avez sélectionné la dimension : {selected_dimension}", {'data': [trace], 'layout': layout}








# Exécution de l'application
if __name__ == '__main__':
    app.run_server(debug=True)
