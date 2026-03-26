import requests
import json
from datetime import datetime

URL = "https://api.open-meteo.com/v1/forecast?latitude=59.33&longitude=18.06&current_weather=true"

def fetch_data():
    response = requests.get(URL)
    response.raise_for_status()
    return response.json()

def save_data(data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/data_{timestamp}.json"

    with open(filename, "w") as f:
        json.dump(data, f)

if __name__ == "__main__":
    data = fetch_data()
    save_data(data)
