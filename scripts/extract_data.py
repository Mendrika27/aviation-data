import requests
import json
from datetime import datetime
from config.api_config import API_KEY  

def extract_flight_data():
    url = "https://test.api.amadeus.com/v2/f/shopping/flight-offers"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch flight data")

if __name__ == "__main__":
    flight_data = extract_flight_data()
    filename = f"flight_data_{datetime.now().strftime('%Y_%m_%d')}.json"
    with open(filename, "w") as f:
        json.dump(flight_data, f)
