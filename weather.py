from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

key = os.environ["WEATHER_API_KEY"]

lat = 49.28803
lon = 4.01619
 


url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={key}"

def fetch_data(url):

    data = requests.get(url)

    data = data.json()

    return data


data = fetch_data(url)

print(data)

