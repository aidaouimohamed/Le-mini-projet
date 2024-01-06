from dash.dependencies import Input, Output
import plotly.express as px
from data_processing import load_data, ajouter_decalage
from graphs import create_map, couleurs_personnalisees

df = load_data()

def register_callbacks(app):
    @app.callback(
        Output('job-map', 'figure'),
        [Input('departement-dropdown', 'value')]
    )
    def update_map(selected_departement):
        if selected_departement is not None:
            filtered_df = df[df['code_departement'] == selected_departement].copy()
            filtered_df = ajouter_decalage(filtered_df)

            center_lat = filtered_df['latitude'].mean()
            center_lon = filtered_df['longitude'].mean()

            return px.scatter_mapbox(
                filtered_df, lat='latitude', lon='longitude',
                hover_name='departement',
                hover_data={'intitule_poste': True, 'type_contrat': True, 'latitude': False, 'longitude': False, 'unique_id': False},
                height=750,
                color='unique_id',
                color_continuous_scale=couleurs_personnalisees,
                zoom=10,
                center={"lat": center_lat, "lon": center_lon},
                mapbox_style='carto-positron'
            )
        else:
            return create_map(df)
