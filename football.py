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


# Function to fetch data from Yahoo API with GET request

def fetch_data_yahoo(url, headers):

    data_get = requests.get(url, headers=headers)

    data_get = data_get.json()

    df = pd.json_normalize(data_get['response']['suggestions'])

    df.to_csv('football.csv', index=False)

    return data_get


data_get = fetch_data_yahoo(url, headers)

print(data_get)
