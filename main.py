import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import aiohttp
import asyncio

app = dash.Dash(__name__)

# Fonction pour normaliser les noms de ville
def normaliser_ville(ville):
    ville = ville.upper()
    regroupements = {
        "ILE-DE-FRANCE": ["PARIS", "PARIS (DEPT.)", "SEINE SAINT DENIS", "NEUILLY SUR SEINE",
                          "ISSY LES MOULINEAUX", "HAUTS DE SEINE", "VAL DE MARNE", "SEINE ET MARNE",
                          "BOULOGNE BILLANCOURT", "LEVALLOIS PERRET", "COURBEVOIE", "VAL D'OISE",
                          "ST DENIS", "YVELINES", "ESSONNE", "MONTREUIL", "ARGENTEUIL", "VERSAILLES",
                          "NANTERRE", "CRETEIL", "AULNAY-SOUS-BOIS", "VITRY-SUR-SEINE", "COLOMBES",
                          "ASNIÈRES-SUR-SEINE", "RUEIL-MALMAISON", "CHAMPIGNY-SUR-MARNE", "SAINT-MAUR-DES-FOSSÉS",
                          "AUBERVILLIERS", "DRANCY", "NOISY-LE-GRAND", "SARCELLES"],
        "RENNES": ["RENNES", "BRUZ"],
        "LYON": ["LYON", "LYON 01"],
        "CAEN": ["CAEN", "HEROUVILLE ST CLAIR"]
    }
    for groupe_principal, villes in regroupements.items():
        if any(env in ville for env in villes):
            return groupe_principal
    return ville

# Fonctions asynchrones pour récupérer les données avec gestion des erreurs de limite de taux
async def fetch_data_with_retry(session, url, params, retries=3, delay=1):
    for i in range(retries):
        async with session.get(url, params=params) as response:
            if response.status == 429:  # Too Many Requests
                await asyncio.sleep(delay)
            else:
                return await response.json()
    return None  # ou gérer l'échec ici

async def get_data_async():
    codes_rome = ['M1810', 'C1102', 'C1206', 'C1502', 'M1503', 'D1106', 'D1211', 'D1401', 'D1505', 'D1507', 'E1103', 'E1107', 'M1204', 'M1205', 'M1501', 'M1502', 'M1605', 'M1607', 'M1705', 'M1805']
    url = "https://labonnealternance.apprentissage.beta.gouv.fr/api/v1/jobs"
    villes = []

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data_with_retry(session, url, {'caller': 'aide_alternance', 'romes': code}) for code in codes_rome]
        responses = await asyncio.gather(*tasks)

        for response in responses:
            if response and 'peJobs' in response and 'results' in response['peJobs']:
                for job in response['peJobs']['results']:
                    city = job['place']['city']
                    ville_normalisee = normaliser_ville(city.split(' - ')[1] if ' - ' in city else city)
                    villes.append(ville_normalisee)
            elif response:
                print("Réponse inattendue de l'API:", response)
            else:
                print("Échec de récupération des données après plusieurs tentatives")

    df_offres = pd.DataFrame(villes, columns=['Ville'])
    df_offres_count = df_offres['Ville'].value_counts().reset_index()
    df_offres_count.columns = ['Ville', 'Nombre d\'Offres']
    df_offres_count = df_offres_count[df_offres_count['Nombre d\'Offres'] > 5]
    return df_offres_count

# Callback for updating the pie chart
@app.callback(
    Output('pie-chart-container', 'children'),
    [Input('interval-component', 'n_intervals')]
)
def update_pie_chart(n):
    df_offres_count = asyncio.run(get_data_async())
    total_offres = df_offres_count['Nombre d\'Offres'].sum()
    
    # Calculate the percentage column
    df_offres_count['Pourcentage'] = (df_offres_count['Nombre d\'Offres'] / total_offres) * 100
    
    # Set the height and width of the pie chart
    fig = px.pie(df_offres_count, names='Ville', values='Pourcentage', title='Répartition des Offres par Ville', height=500, width=700)
    return dcc.Graph(figure=fig)


# Callback for updating the bar chart
@app.callback(
    Output('graph-container', 'children'),
    [Input('interval-component', 'n_intervals')]
)
def update_graph(n):
    df_offres_count = asyncio.run(get_data_async())
    fig = px.bar(df_offres_count, x='Ville', y='Nombre d\'Offres', title='Nombre d\'Offres par Ville')
    return dcc.Graph(figure=fig)

# Layout of the application
app.layout = html.Div([
    html.H1("Dashboard des Offres d'Emploi"),
    dcc.Interval(
        id='interval-component',
        interval=300000,  # Update every 5 minutes
        n_intervals=0
    ),
    html.Div([
        html.Div(id='graph-container', style={'width': '49%', 'display': 'inline-block'}),
        html.Div(id='pie-chart-container', style={'width': '49%', 'display': 'inline-block'})
    ])
])

# Launch the application
if __name__ == '__main__':
    app.run_server(debug=True)