# callbacks1.py
from dash import Input, Output, dcc  # Import necessary modules from Dash framework
import data_processing  # Import the data processing module
import graphs  # Import the graphs module

# Function to register callbacks in the Dash application
def register_callbacks(app):
    # Define a callback function for updating a graph based on a slider input
    @app.callback(
        Output('graph-container', 'children'),  # Output target is the 'graph-container' component
        [Input('min-offre-slider', 'value')]  # Input is the value of 'min-offre-slider'
    )
    # Function to update the graph based on the slider input
    def update_graph(min_offres):
        df = data_processing.lire_donnees_json()  # Read data from a JSON file using the data processing module
        fig = graphs.create_bar_graph(df, min_offres)  # Create a bar graph based on the data and slider value
        return dcc.Graph(figure=fig)  # Return the graph to be displayed in the 'graph-container'
