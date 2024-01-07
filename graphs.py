import pandas as pd
import plotly.express as px

# Function to create a bar graph of job offers by department.
def create_bar_graph(df, min_offres):
    # Counting the number of offers per department and filtering based on the minimum offers.
    filtered_df_count = df['Departement'].value_counts().reset_index()
    filtered_df_count.columns = ['Departement', 'Nombre d\'Offres']
    filtered_df_count = filtered_df_count[filtered_df_count['Nombre d\'Offres'] >= min_offres]

    # Creating a bar plot with the filtered data.
    fig = px.bar(filtered_df_count, x='Departement', y='Nombre d\'Offres', title='Nombre d\'Offres par Département')
    
    # Setting the layout for the plot.
    fig.update_layout(
        width=1400, 
        height=700  # Height of the histogram
    )
    
    return fig

# Function to generate a pie chart for apprenticeship data, optionally filtered by year.
def generate_chart(df_alternance, annee=None):
    # Filtering the dataset by year if provided.
    df_filtered = df_alternance[df_alternance['date'].dt.year == annee] if annee else df_alternance
    df_niveau_count = df_filtered.groupby('niveau_diplome')['effectif_de_jeunes'].sum().reset_index()

    # Custom color palette for the chart.
    custom_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
                     '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

    # Creating a pie chart with the filtered dataset.
    fig = px.pie(df_niveau_count, names='niveau_diplome', values='effectif_de_jeunes', 
                 color_discrete_sequence=custom_colors)
    return fig

# Function to create a bar chart of apprenticeship numbers over different durations.
def create_bar_chart(df):
    # Creating a bar chart with the given data.
    fig = px.bar(df, x='nombre_de_moi', y='effectif_de_jeunes', 
                 title="Nombre d'Alternances par Plage de Durée")
    
    # Customizing the layout of the chart.
    fig.update_layout(
        title={
            'text': "Nombre d'Alternances par Plage de Durée",
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        bargap=0.001,  # Setting the gap between bars.
        width=1300,
        height=500
    )
    return fig

# Custom color palette for various charts.
couleurs_personnalisees = ['#003f5c', '#2f4b7c', '#665191', '#a05195', '#d45087', '#f95d6a', '#ff7c43', '#ffa600']

# Function to create an interactive map with job offer locations.
def create_map(dataframe):
    # Creating a scatter mapbox chart with the given dataframe.
    return px.scatter_mapbox(
        dataframe, lat='latitude', lon='longitude',
        hover_name='departement',
        hover_data={'intitule_poste': True, 'type_contrat': True, 'latitude': False, 'longitude': False, 'unique_id': False},
        height=750,  # Setting the height of the map.
        color='unique_id',  # Using unique_id for color differentiation.
        color_continuous_scale=couleurs_personnalisees,  # Custom color scale.
        zoom=5,  # Initial zoom level of the map.
        mapbox_style='carto-positron'  # Map style.
    )