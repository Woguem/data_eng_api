import requests
import os
import json
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

key = os.environ["RAPIDAPI_KEY_FOOTBALL"]

host = "free-api-live-football-data.p.rapidapi.com"

headers = {
    'x-rapidapi-key': key,
    'x-rapidapi-host': host
}

url = 'https://free-api-live-football-data.p.rapidapi.com/football-players-search?search=m' 


def fetch_data_yahoo(url, headers):

    data = requests.get(url, headers=headers)

    data = data.json()

    df = pd.json_normalize(data['response']['suggestions'])

    df.to_csv('football.csv', index=False)

    return data


data = fetch_data_yahoo(url, headers)

print(data)

