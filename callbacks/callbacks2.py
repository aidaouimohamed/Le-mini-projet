# callbacks2.py
from dash import Input, Output, dcc
import graphs

# This function is used to register callback functions in a Dash app.
def register_callbacks(app):
    # Define a callback function with Dash's decorator.
    @app.callback(
        # Specify the output of the callback: the 'figure' attribute of the component with id 'graphique-alternance'.
        Output('graphique-alternance', 'figure'),
        # Specify the input of the callback: the 'value' attribute of the component with id 'annee-selector'.
        [Input('annee-selector', 'value')]
    )
    # This function is called whenever the input value changes.
    def update_chart(selected_year):
        # Access the dataframe stored in the app's server configuration.
        df_alternance = app.server.config['df_alternance']
        # Call the function to generate a chart based on the selected year and return the chart figure.
        return graphs.generate_chart(df_alternance, selected_year)
