import json
import pandas as pd
import plotly.express as px
from dash import dcc, html, Dash, Input, Output, ctx

app = Dash(__name__)

# Assuming 'data_alternance.json' is in the same directory as the script
def lire_donnees_alternance(fichier='data_alternance.json'):
    with open(fichier, 'r') as file:
        data = json.load(file)

    alternances = []
    for record in data:
        fields = record['fields']
        alternances.append({
            'effectif_de_jeunes': fields['effectif_de_jeunes'],
            'duree_alternance': fields['duree_alternance']
        })

    return pd.DataFrame(alternances)

df_alternance = lire_donnees_alternance()

# Categorize 'duree_alternance' into nombre_de_mois and sum 'effectif_de_jeunes' for each nombre_de_moi
df_alternance['nombre_de_moi'] = pd.cut(df_alternance['duree_alternance'], 
                                bins=[6, 12, 24, 36, 40], 
                                labels=['6', '12', '24', '36'], 
                                right=False)

df_nombre_de_moi_count = df_alternance.groupby('nombre_de_moi', observed=True)['effectif_de_jeunes'].sum().reset_index()

# Create the bar chart
fig = px.bar(df_nombre_de_moi_count, x='nombre_de_moi', y='effectif_de_jeunes', 
             title="Nombre d'Alternances par Plage de Durée")

# Ajustement de l'espacement entre les barres
fig.update_layout(bargap=0.001)  # Réglage de l'espacement entre les barres

app.layout = html.Div([
    html.H1("Histogramme des Alternances par Plage de Durée"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)