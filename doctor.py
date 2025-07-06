import requests
import os
import json
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

key = os.environ["RAPIDAPI_KEY_DOCTOR"]

host = "doctors-consultation.p.rapidapi.com"

headers = {
    'Content-Type': 'application/json',
    'x-rapidapi-key': key,
    'x-rapidapi-host': host
}

url = 'https://doctors-consultation.p.rapidapi.com/Crm/ObterMedicoLista'



data = [{"uf":"GO","numCrm":15587},
        {"uf":"MG","numCrm":19785},
        {"uf":"BA","numCrm":38106},
        {"uf":"AL","numCrm":5503},
        {"uf":"AP","numCrm":610},
        {"uf":"CE","numCrm":22140},
        {"uf":"DF","numCrm":23103},
        {"uf":"ES","numCrm":10286}]


# Funtion to send a POST request to the API

def send_data_to_server(url, data, headers):

    response = requests.post(url, json=data, headers=headers)

    return response


response = send_data_to_server(url, data, headers)

print(f"Response status code: {response.status_code}")

print(f"Response content: {response.content}")




