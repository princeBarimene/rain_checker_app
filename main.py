import requests
from dotenv import load_dotenv
import os
import json
from pprint import pprint

load_dotenv()  # take environment variables from .env.

API_KEY = os.getenv('api_key')
lat = os.getenv('lat')
lon = os.getenv('lon') 

url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}"


response = requests.get(url=url)

data = response.json()



