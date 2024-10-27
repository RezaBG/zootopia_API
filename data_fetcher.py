import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")

def fetch_data(animal_name):
    """Fetch animal data from the API based on the animal name."""
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    response = requests.get(api_url, headers={"X-Api-Key": API_KEY})

    if response.status_code == requests.codes.ok:
        try:
            return response.json()
        except ValueError:
            print("Error: Could not parse JSON response")
            return None
    else:
        print("Error fetching data from the API.")
        return None