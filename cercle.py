import json
import pandas as pd
import plotly.express as px
from dash import dcc, html, Dash, Input, Output

app = Dash(__name__)
app.title = "Statistiques des Alternances"

# Lecture du fichier JSON
def lire_donnees_alternance(fichier='data_alternance.json'):
    alternances = []
    with open(fichier, 'r') as file:
        data = json.load(file)
        for record in data:
            fields = record['fields']
            alternances.append({
                'niveau_diplome': fields['lib_court_niveau_diplome'],
                'effectif_de_jeunes': fields['effectif_de_jeunes'],
                'date': fields['date']
            })
    return pd.DataFrame(alternances)

df_alternance = lire_donnees_alternance()
df_alternance['date'] = pd.to_datetime(df_alternance['date'])
annees = df_alternance['date'].dt.year.unique()

# Fonction pour générer le graphique basé sur le filtre
def generate_chart(annee=None):
    df_filtered = df_alternance[df_alternance['date'].dt.year == annee] if annee else df_alternance
    df_niveau_count = df_filtered.groupby('niveau_diplome')['effectif_de_jeunes'].sum().reset_index()

    # Palette de couleurs personnalisée
    custom_colors = [
        '#1f77b4',  # Bleu
        '#ff7f0e',  # Orange
        '#2ca02c',  # Vert
        '#d62728',  # Rouge
        '#9467bd',  # Violet
        '#8c564b',  # Marron
        '#e377c2',  # Rose
        '#7f7f7f',  # Gris
        '#bcbd22',  # Olive
        '#17becf'   # Cyan
    ]

    fig = px.pie(df_niveau_count, names='niveau_diplome', values='effectif_de_jeunes', 
                 color_discrete_sequence=custom_colors)
    return fig

# Layout de l'application avec des styles CSS
app.layout = html.Div([
    html.H1("Statistiques des Alternances", style={'textAlign': 'center'}),
    html.Div([
        html.Label("Sélectionnez une année :"),
        dcc.Dropdown(
            id='annee-selector',
            options=[{'label': annee, 'value': annee} for annee in annees],
            value=annees[0],
            clearable=False
        ),
    ], style={'width': '48%', 'display': 'inline-block'}),
    dcc.Graph(id='graphique-alternance')
], style={'padding': 50})

# Callback pour mettre à jour le graphique en fonction de l'année sélectionnée
@app.callback(
    Output('graphique-alternance', 'figure'),
    [Input('annee-selector', 'value')]
)
def update_chart(selected_year):
    return generate_chart(selected_year)

if __name__ == '__main__':
    app.run_server(debug=True)
