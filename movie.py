import requests
import os
import json
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

key = os.environ["RAPIDAPI_KEY_MOVIE"]

host = "netflix54.p.rapidapi.com"

headers = {
    'x-rapidapi-key': key,
    'x-rapidapi-host': host
}

url = 'https://netflix54.p.rapidapi.com/season/episodes/?ids=80077209%2C80117715&offset=0&limit=25&lang=en' 


def fetch_data_yahoo(url, headers):

    data = requests.get(url, headers=headers)

    data = data.json()

    df = pd.json_normalize(data[0]["episodes"])

    df.to_csv('movie.csv', index=False)

    return data[0]


data = fetch_data_yahoo(url, headers)

print(data)

