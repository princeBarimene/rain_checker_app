import requests
from dotenv import load_dotenv
import os
import json
from pprint import pprint
from twilio.rest import Client

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

will_rain = False
for hour_data in data['list']:
    condition_code = hour_data['weather'][0]['id']
    if  condition_code < 700:
        will_rain = True

if will_rain:
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_=f'whatsapp:{os.environ["free_number_from_twilio"]}',
    body="It's going to rain today. Remember to bring an umbrella",
   
    to=f'whatsapp:{os.environ["target_phone_nunmber"]}')

    print(message.status)
else:
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_=f'whatsapp:{os.environ["free_number_from_twilio"]}',
    body="It won't rain today... Its our lucky day.",
   
    to=f'whatsapp:{os.environ["target_phone_nunmber"]}')

    print(message.status)
    







    
    





