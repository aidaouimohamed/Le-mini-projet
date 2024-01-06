# callbacks1.py
from dash import Input, Output, dcc
import data_processing
import graphs

def register_callbacks(app):
    @app.callback(
        Output('graph-container', 'children'),
        [Input('min-offre-slider', 'value')]
    )
    def update_graph(min_offres):
        df = data_processing.lire_donnees_json()
        fig = graphs.create_bar_graph(df, min_offres)
        return dcc.Graph(figure=fig)
