import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import requests
import plotly.graph_objs as go

# Fonction pour récupérer les données depuis l'API
def get_data(api_url):
    response = requests.get(api_url)
    response.raise_for_status()  # Lève une exception pour les codes HTTP d'erreur
    data = response.json()
    return data['value']




# Configuration de l'application Dash
app = dash.Dash(__name__)





# URL de l'API
api_url = "https://ghoapi.azureedge.net/api/WHOSIS_000001?$filter=Dim1%20eq%20%27MLE%27"
data = get_data(api_url)





# Mise en page du dashboard
app.layout = html.Div([
    html.H1("WHO API Dashboard"),

    dcc.Graph(id='dimension-graph'),

    html.Div(id='selected-dimension'),
])





# Callback pour mettre à jour l'affichage
@app.callback(
    [Output('selected-dimension', 'children'),
     Output('dimension-graph', 'figure')],
    [Input('dimension-graph', 'hoverData')]
)
def update_selected_dimension(hover_data):
    # Vous pouvez utiliser hover_data pour afficher des informations supplémentaires lorsqu'un point est survolé.
    if hover_data:
        print(f"Hover data: {hover_data}")

    # Assurez-vous que les noms de clés correspondent à la structure réelle des données
    x_data = [entry.get('Year', 0) for entry in data]
    y_data = [entry.get('Value', 0) for entry in data]

    # Création de la trace de la courbe
    trace = go.Scatter(
        x=x_data,
        y=y_data,
        mode='lines+markers',
        name='Courbe de la dimension'
    )

    layout = go.Layout(
        title="Courbe de la dimension",
        xaxis=dict(title='Année'),
        yaxis=dict(title='Valeur')
    )

    return "Vous avez sélectionné la dimension : MLE", {'data': [trace], 'layout': layout}




# Exécution de l'application
if __name__ == '__main__':
    app.run_server(debug=True)
