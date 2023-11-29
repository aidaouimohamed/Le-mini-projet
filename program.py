import requests

def get_who_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Lève une exception pour les codes HTTP d'erreur
        data = response.json()
        return data
    except requests.exceptions.HTTPError as errh:
        print(f"Erreur HTTP : {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Erreur de connexion : {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout de la requête : {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Erreur lors de la requête : {err}")

if __name__ == "__main__":
    api_url = "https://ghoapi.azureedge.net/api/Dimension"
    
    data = get_who_data(api_url)

    if data:
        print(data)
