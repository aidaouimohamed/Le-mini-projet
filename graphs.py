import pandas as pd
import plotly.express as px

# Fonction du fichier 1
def create_bar_graph(df, min_offres):
    filtered_df_count = df['Departement'].value_counts().reset_index()
    filtered_df_count.columns = ['Departement', 'Nombre d\'Offres']
    filtered_df_count = filtered_df_count[filtered_df_count['Nombre d\'Offres'] >= min_offres]

    fig = px.bar(filtered_df_count, x='Departement', y='Nombre d\'Offres', title='Nombre d\'Offres par Département')
    return fig

# Fonction du fichier 2
def generate_chart(df_alternance, annee=None):
    df_filtered = df_alternance[df_alternance['date'].dt.year == annee] if annee else df_alternance
    df_niveau_count = df_filtered.groupby('niveau_diplome')['effectif_de_jeunes'].sum().reset_index()

    custom_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
                     '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

    fig = px.pie(df_niveau_count, names='niveau_diplome', values='effectif_de_jeunes', 
                 color_discrete_sequence=custom_colors)
    return fig

def create_bar_chart(df):
    fig = px.bar(df, x='nombre_de_moi', y='effectif_de_jeunes', 
                 title="Nombre d'Alternances par Plage de Durée")
    fig.update_layout(bargap=0.001)
    return fig


couleurs_personnalisees = ['#003f5c', '#2f4b7c', '#665191', '#a05195', '#d45087', '#f95d6a', '#ff7c43', '#ffa600']

def create_map(dataframe):
    return px.scatter_mapbox(
        dataframe, lat='latitude', lon='longitude',
        hover_name='departement',
        hover_data={'intitule_poste': True, 'type_contrat': True, 'latitude': False, 'longitude': False, 'unique_id': False},
        height=750,
        color='unique_id',
        color_continuous_scale=couleurs_personnalisees,
        zoom=5,
        mapbox_style='carto-positron'
    )
