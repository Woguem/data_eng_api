import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

key = os.environ["RAPIDAPI_KEY"]

host = "meteostat.p.rapidapi.com"

headers = {
    'x-rapidapi-key': key,
    'x-rapidapi-host': host
}

url = 'https://meteostat.p.rapidapi.com/stations/hourly?station=10637&start=2020-01-01&end=2020-01-01&tz=Europe%2FBerlin' 

def fetch_data(url, headers) :

    data = requests.get(url, headers = headers)

    data = data.json()

    return data


data = fetch_data(url, headers)

print(data)






