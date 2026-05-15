import requests
import json
from datetime import datetime
import os
import pandas as pd

URL = "https://api.open-meteo.com/v1/forecast?latitude=59.33&longitude=18.06&current_weather=true"

def fetch_weather():
    response = requests.get(URL)
    if response.status_code != 200:
        raise Exception(f"API request failed: {response.status_code}")
    return response.json()

def transform_data(raw_data):
    current = raw_data.get("current_weather", {})
    transformed = {
        "timestamp": current.get("time"),
        "temperature": current.get("temperature"),
        "windspeed": current.get("windspeed"),
        "winddirection": current.get("winddirection"),
    }
    return transformed

def save_to_json(data):
    os.makedirs("data", exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"data/weather_{today}.json"
    
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Data saved to {filename}")

def save_raw_data(raw_data):
    os.makedirs("data/raw", exist_ok=True)
    
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"data/raw/raw_weather_{today}.json"
    
    with open(filename, "w") as f:
        json.dump(raw_data, f)
    print(f"Data saved to {filename}")

def save_to_csv(data):
    os.makedirs("data/csv", exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"data/csv/weather_{today}.csv"

    df = pd.DataFrame([data])
    df.to_csv(filename, index=False)

    print(f"CSV saved to {filename}")


def run_pipeline():
    raw_data = fetch_weather()
    cleaned_data = transform_data(raw_data)
    save_raw_data(raw_data)
    save_to_json(cleaned_data)
    save_to_csv(cleaned_data)

if __name__ == "__main__":
    run_pipeline()

