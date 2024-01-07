from dash.dependencies import Input, Output
import plotly.express as px
from data_processing import load_data, ajouter_decalage
from graphs import create_map, couleurs_personnalisees

df = load_data()  # Load the dataset into a DataFrame

def register_callbacks(app):
    # This function registers callbacks for the Dash app
    @app.callback(
        Output('job-map', 'figure'),  # Output is the map figure
        [Input('departement-dropdown', 'value')]  # Input is the value selected in the dropdown
    )
    def update_map(selected_departement):
        # Function to update the map based on the selected department
        if selected_departement is not None:
            # If a department is selected
            filtered_df = df[df['code_departement'] == selected_departement].copy()
            # Filter the DataFrame based on the selected department
            filtered_df = ajouter_decalage(filtered_df)
            # Adjust the filtered DataFrame with a specific function

            center_lat = filtered_df['latitude'].mean()  # Calculate the average latitude
            center_lon = filtered_df['longitude'].mean()  # Calculate the average longitude

            return px.scatter_mapbox(
                filtered_df, lat='latitude', lon='longitude',
                hover_name='departement',  # Department name will be shown on hover
                hover_data={'intitule_poste': True, 'type_contrat': True, 'latitude': False, 'longitude': False, 'unique_id': False},
                height=750,  # Height of the map
                color='unique_id',  # Color of the markers
                color_continuous_scale=couleurs_personnalisees,  # Custom color scale
                zoom=10,  # Initial zoom level
                center={"lat": center_lat, "lon": center_lon},  # Center of the map
                mapbox_style='carto-positron'  # Style of the map
            )
        else:
            # If no department is selected, display the default map
            return create_map(df)
