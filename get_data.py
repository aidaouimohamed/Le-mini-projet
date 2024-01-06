import requests
import json

def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def save_data_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

url = "https://www.data.gouv.fr/fr/datasets/r/0aba1710-168c-4ec2-a6e2-4ac95df8a63d"
data = get_data(url)

if data:
    save_data_to_file(data, 'niveau.json')
    print("Données téléchargées et sauvegardées dans 'niveau.json'")
else:
    print("Erreur lors du téléchargement des données.")
