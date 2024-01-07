import requests
import json

# Function to retrieve data from a given URL.
def get_data(url):
    response = requests.get(url)  # Send a GET request to the URL.
    if response.status_code == 200:  # Check if the request was successful (HTTP 200 OK).
        return response.json()  # Return the data in JSON format.
    else:
        return None  # Return None if the request was not successful.

# Function to save data to a file in JSON format.
def save_data_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:  # Open a file to write.
        json.dump(data, file, ensure_ascii=False, indent=4)  # Write data in JSON format.

# List of URLs to download data from.
urls = [
    "https://drive.google.com/uc?id=1Xp-sXJjOEwmKEeTqzLiql6dGMEQizgzM",
    "https://drive.google.com/uc?id=1fIVsA_vQUAHO5tYtbfJX5yG8sc8ITNCH",
    "https://drive.google.com/uc?id=18qQVWj-UnGu6CeNYXmA4oBVUJZZxbS1j"
]

# Loop through each URL in the list.
for i, url in enumerate(urls):
    data = get_data(url)  # Retrieve data from the URL.
    if data:
        filename = f'data_{i}.json'  # Create a filename for the data.
        save_data_to_file(data, filename)  # Save the data to a file.
        print(f"Données téléchargées et sauvegardées dans '{filename}'")  # Print a success message.
    else:
        print(f"Erreur lors du téléchargement des données depuis {url}.")  # Print an error message if download fails.
