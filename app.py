from dash import Dash
from dash import html
import dash_bootstrap_components as dbc
import pandas as pd  # Importation de pandas nécessaire pour le traitement des données
import layout.layout1 as layout1  # Importation du layout du fichier 1
import layout.layout2 as layout2  # Importation du layout du fichier 2
import layout.layout3 as layout3  # Importation du layout du fichier 3
import layout.layout4 as layout4  # Importation du layout du fichier 4
from layout.layout4 import create_layout
import callbacks.callbacks1 as callbacks1  # Importation des callbacks du fichier 1
import callbacks.callbacks2 as callbacks2  # Importation des callbacks du fichier 2
import callbacks.callbacks3 as callbacks3  # Importation des callbacks du fichier 1
from callbacks.callbacks3 import register_callbacks
import data_processing  # Importation nécessaire pour le traitement des données

# Initialisation de l'application Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Statistiques des Alternances"

# Configuration spécifique au fichier 2
df_alternance = data_processing.lire_donnees()
df_alternance['date'] = pd.to_datetime(df_alternance['date'])
app.server.config['df_alternance'] = df_alternance
app.server.config['annees'] = df_alternance['date'].dt.year.unique()

# Création du layout combiné
combined_layout = html.Div([
    layout1.create_layout(),
    layout2.create_layout(app),
    layout3.create_layout(),
    layout4.create_layout()
])

app.layout = combined_layout

# Enregistrement des callbacks
callbacks1.register_callbacks(app)  # Callbacks du fichier 1
callbacks2.register_callbacks(app)  # Callbacks du fichier 2
callbacks3.register_callbacks(app)  # Callbacks du fichier 3

# Lancement du serveur
if __name__ == '__main__':
    app.run_server(debug=True)
