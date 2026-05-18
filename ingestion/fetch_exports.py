import requests
import json

def fetch_export_data(country_code, per_page = 10):
    url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/TX.VAL.MRCH.CD.WT"
    
    params = {
        "format": "json",
        "per_page": per_page
    }

    response = requests.get(url, params=params)

    print(f"Status code: {response.status_code}")
    print(json.dumps(response.json(), indent=2))


fetch_export_data("US")