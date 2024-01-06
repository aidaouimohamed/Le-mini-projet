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

urls = [
    "https://drive.google.com/uc?id=1V4rR4F1seaqc0T7aHup1tWPoLQJ6acN3",
    "https://drive.google.com/uc?id=18qQVWj-UnGu6CeNYXmA4oBVUJZZxbS1j",
    "https://drive.google.com/uc?id=18qQVWj-UnGu6CeNYXmA4oBVUJZZxbS1j"
]

for i, url in enumerate(urls):
    data = get_data(url)
    if data:
        filename = f'data_{i}.json'
        save_data_to_file(data, filename)
        print(f"Données téléchargées et sauvegardées dans '{filename}'")
    else:
        print(f"Erreur lors du téléchargement des données depuis {url}.")
