#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.
import json
import requests
import sys
import os
import pprint
from dotenv import load_dotenv

# Load environmental variables
load_dotenv()

APPID = os.environ.get('OPENWEATHER_APIKEY')
print(APPID)

# Computer location from command line arguments
# if len(sys.argv) < 2:
#     print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
#     sys.exit()
# location = ''.join(sys.argv[1:])
location = 'Dallas'


# Download the JSON data from OpenWeatherMap.org's API.
url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={APPID}'
response = requests.get(url)
response.raise_for_status()

# Uncomment to see the raw JSON text:
#print(response.text)

weatherData = json.loads(response.text)


w = weatherData['main']
pprint.pprint(w)

# print(f'Current weather in {location}:')
# print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
# print()
# print('Tomorrow')
# print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])