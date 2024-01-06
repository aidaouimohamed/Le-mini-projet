import json
import pandas as pd
import plotly.express as px
from dash import dcc, html, Dash, Input, Output, ctx

app = Dash(__name__)

def charger_departements(fichier='departement.json'):
    with open(fichier, 'r') as file:
        data = json.load(file)
    return {dep['DEP']: dep['NCC'] for dep in data}

departements = charger_departements()


def lire_donnees_json():
    with open('data.json', 'r') as file:
        responses = json.load(file)

    infos_departements = []
    for response in responses:
        if response and 'peJobs' in response and 'results' in response['peJobs']:
            for job in response['peJobs']['results']:
                if 'zipCode' in job['place']:
                    code_dep = job['place']['zipCode'][:2]
                    # Exclure les départements commençant par 97
                    if code_dep.startswith('97'):
                        continue
                    nom_dep = departements.get(code_dep, 'Inconnu')
                    infos_departements.append({'Departement': f"{code_dep} - {nom_dep}"})

    return pd.DataFrame(infos_departements)


df = lire_donnees_json()

app.layout = html.Div([
    html.H1("Dashboard des Offres d'Emploi par Département"),
    dcc.Slider(
        id='min-offre-slider',
        min=0,
        max=df['Departement'].value_counts().max(),
        value=5,
        marks={i: str(i) for i in range(0, df['Departement'].value_counts().max() + 1, 5)},
        step=1
    ),
    html.Div(id='graph-container')
])

@app.callback(
    Output('graph-container', 'children'),
    [Input('min-offre-slider', 'value')]
)
def update_graph(min_offres):
    filtered_df_count = df['Departement'].value_counts().reset_index()
    filtered_df_count.columns = ['Departement', 'Nombre d\'Offres']
    filtered_df_count = filtered_df_count[filtered_df_count['Nombre d\'Offres'] >= min_offres]
    fig = px.bar(filtered_df_count, x='Departement', y='Nombre d\'Offres', title='Nombre d\'Offres par Département')
    return dcc.Graph(figure=fig)

if __name__ == '__main__':
    app.run_server(debug=True)