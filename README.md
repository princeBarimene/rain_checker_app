
# Rain Checker Application.

This is a python project and application that uses the openweather api to request data and checks whether it will rain or not based on some weather condition code.



## API Reference

#### Get all items

```http
  GET /api.openweathermap.org/data/2.5/forecast
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `appid` | `string` | **Required**. Your API key |
| `lat`   | `float`  | **Required**. Latitude (location). You can get your latitude and longitutude from the website [latlong.net](https://www.latlong.net)    |
| `lon`   | `float`  | **Required**. Longitude (Location)   |
| `cnt`   | `int`    | **OPTIONAL**. Number of results returned. |


#### You will also need to register an account with Twilio to send SMS notifications from a phone number to your target phone number. 

## Optional
I used pythonAnywhere to schedule the python application as a script to be ran every 6AM to trigger notifications.

    
## Run Locally

Clone the project

```bash
  git clone https://github.com/princeBarimene/rain_checker_app
```

Go to the project directory

```bash
  cd rain_checker_app

```
Create a Virtual Environment and Source into it

```bash
  python -m  venv venv
  source venv/bin/activate
```


Install dependencies

```bash
  pip install -r requirements.txt
```

Run the Code Locally

```bash
  python main.py
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`api_key`

`lat`

`lon`

`TWILIO_ACCOUNT_SID`

`TWILIO_AUTH_TOKEN`

`free_number_from_twilio`

`target_phone_nunmber`


## Authors

- [@princebarimene](https://www.github.com/princeBarimene)


## Contributing

Contributions are always welcome!
You can reach out to me through github or my email.


## Feedback

If you have any feedback, please reach out to me at prince.g.olubari@gmail.com


## Screenshots

![App Screenshot](/screenshots/twilio_screenshot.jpg)


## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)
 - [Angela Yu](https://github.com/angelabauer)
 

 ## Future Improvements
 - I am hoping to improve the request to include other weather conditions.
 - Probably build a mobile app that can alert me about weather conditons every hour or 3 hours.