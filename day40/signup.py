#!/usr/bin/env python

import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = f"https://api.sheety.co/{os.getenv('SHEETY_ID')}"
print("Welcome to dpnet.ca Flight Club")
print("We find the best flight deals and email you.")

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
valid_email = False
while not valid_email:
    email = input("What is your email? ")
    confirm_email = input("Please type your email again. ")
    if email == confirm_email:
        valid_email = True

headers = {
    "Authorization": f"Bearer {os.getenv('SHEETY_API_KEY')}",
    "Accept": "application/json",
    "Content-Type": "application/json",
}

body = {
    "user": {"firstName": first_name, "lastName": last_name, "email": email}
}

url = BASE_URL + "/users"
result = requests.post(url, headers=headers, json=body)
result.raise_for_status()
print("You're in the club! ")
