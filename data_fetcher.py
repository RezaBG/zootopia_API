import requests

API_KEY = '6+4pkl60Nmam4U8+D3zbMQ==P4rsYPQkdBa2PyhR'


def fetch_data(animal_name):
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)
    response = requests.get(api_url, headers={"X-Api-Key": API_KEY})

    if response.status_code == requests.codes.ok:
        try:
            print("Raw Response Text:")
            print(response.text)
            return response.json()
        except ValueError:
            print("Error: Could not parse the JSON response")
            return None
    else:
        print("Error")
        return None


