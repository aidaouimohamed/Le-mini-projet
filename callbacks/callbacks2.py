# callbacks2.py
from dash import Input, Output, dcc
import graphs

def register_callbacks(app):
    @app.callback(
        Output('graphique-alternance', 'figure'),
        [Input('annee-selector', 'value')]
    )
    def update_chart(selected_year):
        df_alternance = app.server.config['df_alternance']
        return graphs.generate_chart(df_alternance, selected_year)
