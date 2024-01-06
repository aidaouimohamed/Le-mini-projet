import json
import pandas as pd
import numpy as np


def charger_departements(fichier='data_2.json'):
    with open(fichier, 'r') as file:
        data = json.load(file)
    return {dep['DEP']: dep['NCC'] for dep in data}

def lire_donnees_json():
    departements = charger_departements()

    with open('data_0.json', 'r') as file:
        responses = json.load(file)

    infos_departements = []
    for response in responses:
        if response and 'peJobs' in response and 'results' in response['peJobs']:
            for job in response['peJobs']['results']:
                if 'zipCode' in job['place']:
                    code_dep = job['place']['zipCode'][:2]
                    if code_dep.startswith('97'):
                        continue
                    nom_dep = departements.get(code_dep, 'Inconnu')
                    infos_departements.append({'Departement': f"{code_dep} - {nom_dep}"})

    return pd.DataFrame(infos_departements)

def lire_donnees(fichier='data_1.json'):
    alternances = []
    with open(fichier, 'r') as file:
        data = json.load(file)
        for record in data:
            fields = record['fields']
            alternances.append({
                'niveau_diplome': fields['lib_court_niveau_diplome'],
                'effectif_de_jeunes': fields['effectif_de_jeunes'],
                'date': fields['date']
            })
    return pd.DataFrame(alternances)

def lire_donnees_alternance(fichier='data_1.json'):
    with open(fichier, 'r') as file:
        data = json.load(file)

    alternances = []
    for record in data:
        fields = record['fields']
        alternances.append({
            'effectif_de_jeunes': fields['effectif_de_jeunes'],
            'duree_alternance': fields['duree_alternance']
        })

    return pd.DataFrame(alternances)

def process_data():
    df_alternance = lire_donnees_alternance()
    df_alternance['nombre_de_moi'] = pd.cut(df_alternance['duree_alternance'], 
                                            bins=[6, 12, 24, 36, 40], 
                                            labels=['6', '12', '24', '36'], 
                                            right=False)
    df_nombre_de_moi_count = df_alternance.groupby('nombre_de_moi', observed=True)['effectif_de_jeunes'].sum().reset_index()
    return df_nombre_de_moi_count

# Fonction pour ajouter un léger décalage aléatoire aux coordonnées
def ajouter_decalage(df, colonnes=['latitude', 'longitude'], decalage_max=0.009):
    for col in colonnes:
        df[col] = df[col].apply(lambda x: x + np.random.uniform(-decalage_max, decalage_max))
    return df

def load_data():
    departements = charger_departements()

    with open('data_0.json', 'r') as file:
        responses = json.load(file)

    infos_departements = []
    for response in responses:
        if response and 'peJobs' in response and 'results' in response['peJobs']:
            for job in response['peJobs']['results']:
                if 'zipCode' in job['place']:
                    code_dep = job['place']['zipCode'][:2]
                    if code_dep.startswith('97'):
                        continue
                    job['place']['code_departement'] = code_dep
                    job['place']['departement'] = departements.get(code_dep, 'Inconnu')
                    job['place']['intitule_poste'] = job['title'] if 'title' in job else 'Inconnu'
                    job['place']['type_contrat'] = job['job']['contractType'] if 'job' in job and 'contractType' in job['job'] else 'Inconnu'
                    infos_departements.append(job['place'])

    df = pd.DataFrame(infos_departements)
    df['unique_id'] = df.index
    df = ajouter_decalage(df)
    return df
