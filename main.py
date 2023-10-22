# https://docs.google.com/spreadsheets/d/1_X2QcBAdb8G0RtKKBZ4jXSUezKveChEiCGFcSUhHYOw/edit#gid=0
import requests
from datetime import datetime
import os

APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')
URL_ENDPOINT = os.environ.get('URL_ENDPOINT')
SHEETY_ENDPOINT = os.environ.get('SHEETY_ENDPOINT')
TOKEN = os.environ.get('TOKEN')
GENDER = "FEMALE"
WEIGHT_KG = 56
HEIGHT = "175"
AGE = "18"

excercise_endpoint = f"{URL_ENDPOINT}/v2/natural/exercise"

excercise_input = input("Tell me which exercise you did today: ")

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": excercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=excercise_endpoint, json=parameters, headers=header)
response.raise_for_status()
result = response.json()

for exercise in result['exercises']:
    date = datetime.now().strftime("%Y%m%d")
    time = datetime.now().strftime("%H:%M:%S")
    excercise_name = exercise['name'].title()
    duration = exercise['duration_min']
    calories = exercise['nf_calories']

# date = datetime.now().strftime("%Y%m%d")
# time = datetime.now().strftime("%H:%M:%S")
# excercise_name = result['exercises'][0]['name'].title()
# duration = result['exercises'][0]['duration_min']
# calories = result['exercises'][0]['nf_calories']

    sheety_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": excercise_name,
            "duration": duration,
            "calories": calories,
        }
    }

    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_params, headers=headers)
    sheety_response.raise_for_status()
    result_sheety = sheety_response.text