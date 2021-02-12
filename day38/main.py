#!/usr/bin/env python

import os
import requests
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()

BASE_URL = "https://trackapi.nutritionix.com/v2"

query = input("Enter excercise: ")

headers = {
    "x-app-id": os.getenv("APP_ID"),
    "x-app-key": os.getenv("API_KEY"),
    "x-remote-user-id": "0",
}
endpoint = "/natural/exercise"

body = {
    "query": query,
    "gender": os.getenv("GENDER"),
    "weight_kg": int(os.getenv("WEIGHT")),
    "height_cm": int(os.getenv("HEIGHT")),
    "age": int(os.getenv("AGE")),
}
response = requests.post(BASE_URL + endpoint, headers=headers, json=body)
exercises = response.json()
exercises = exercises["exercises"]


now = datetime.now()
date = now.strftime("%d/%m/%Y")
# time = now.strftime("%H:%M:%S")
time = now.strftime("%X")

sheety_url = f"https://api.sheety.co/{os.getenv('SHEETY_PROJECT')}"
for exercise in exercises:
    sheet_body = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheet_headers = {"Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}"}
    sheet_response = requests.post(
        sheety_url, headers=sheet_headers, json=sheet_body
    )
