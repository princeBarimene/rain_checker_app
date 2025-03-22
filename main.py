import requests
from dotenv import load_dotenv
import os
import json
from pprint import pprint

load_dotenv()  # take environment variables from .env.

OWM_Endpoint ="https://api.openweathermap.org/data/2.5/forecast"
weather_params = {
    "appid" : os.getenv('api_key'),
    "lat" : os.getenv('lat'),
    "lon" : os.getenv('lon'), 
    "cnt" : 4
}


response = requests.get(OWM_Endpoint, params=weather_params)

data = response.json()




