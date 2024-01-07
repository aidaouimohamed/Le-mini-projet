from dash import Dash
from dash import html
import dash_bootstrap_components as dbc
import pandas as pd
import layout.layout1 as layout1
import layout.layout2 as layout2
import layout.layout3 as layout3
import layout.layout4 as layout4
from layout.layout4 import create_layout
import callbacks.callbacks1 as callbacks1
import callbacks.callbacks2 as callbacks2
import callbacks.callbacks3 as callbacks3
from callbacks.callbacks3 import register_callbacks
import data_processing

# Initialize the Dash app with Bootstrap styles
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Statistiques des Alternances"  # Set the title of the web application

# Data processing and configuration
df_alternance = data_processing.lire_donnees()  # Read data for the application
df_alternance['date'] = pd.to_datetime(df_alternance['date'])  # Convert 'date' column to datetime format
app.server.config['df_alternance'] = df_alternance  # Store data in server config for global access
app.server.config['annees'] = df_alternance['date'].dt.year.unique()  # Store unique years for global access

# Creating the overall layout of the app by combining individual layouts from different modules
combined_layout = html.Div([
    layout1.create_layout(),  # Layout from layout1 module
    layout2.create_layout(app),  # Layout from layout2 module
    layout3.create_layout(),  # Layout from layout3 module
    layout4.create_layout()  # Layout from layout4 module
])

app.layout = combined_layout  # Set the combined layout as the app's layout

# Registering callbacks for interactivity
callbacks1.register_callbacks(app)  # Register callbacks from callbacks1 module
callbacks2.register_callbacks(app)  # Register callbacks from callbacks2 module
callbacks3.register_callbacks(app)  # Register callbacks from callbacks3 module

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)  # Start the server with debug mode on
