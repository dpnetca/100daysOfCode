import os
import requests
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    def __init__(self):
        self.base_url = f"https://api.sheety.co/{os.getenv('SHEETY_ID')}"
        self.headers = {
            "Authorization": f"Bearer {os.getenv('SHEETY_API_KEY')}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        self.sheet_data = []

    def read_sheet(self):
        """read google sheet using sheety and store in class attribute"""
        sheet = "/prices"
        response = requests.get(self.base_url + sheet, headers=self.headers)
        data = response.json()
        self.sheet_data = data["prices"]

    def update_iata(self, object_id, iata):
        """update IATA CODE in google sheet

        Args:
            object_id (int): row / obejct to update
            iata (str): iata code
        """
        url = f"{self.base_url}/prices/{object_id}"
        body = {"price": {"iataCode": iata}}
        requests.put(url, headers=self.headers, json=body)
