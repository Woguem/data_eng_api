import requests
import os
import json
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

key = os.environ["RAPIDAPI_KEY_FOOD"]

host = "uber-eats-scraper-api.p.rapidapi.com"

headers = {
    'Content-Type': 'application/json',
    'x-rapidapi-key': key,
    'x-rapidapi-host': host
}

url = 'https://uber-eats-scraper-api.p.rapidapi.com/api/job'



data = {"scraper":{"maxRows":15,
                  "query":"Pizza",
                  "address":"1600 Pennsylvania Avenue, Washington DC",
                  "locale":"en-US",
                  "page":1}}


# Funtion to send a POST request to the API

def send_data_to_server(url, data, headers):

    response = requests.post(url, json=data, headers=headers)

    return response


response = send_data_to_server(url, data, headers)

print(f"Response status code: {response.status_code}")

print(f"Response content: {response.content}")




