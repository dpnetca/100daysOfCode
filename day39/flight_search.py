import os
import requests
from dotenv import load_dotenv

from flight_data import FlightData

load_dotenv()


class FlightSearch:
    def __init__(self):
        self.url_base = "https://tequila-api.kiwi.com"
        self.headers = {
            "apikey": os.getenv("KIWI_API_KEY"),
            "accept": "application/json",
        }

    # NOTES:
    # refactored after looking at instructor solution to:
    # 1 - pass from and to dates in, instead of determining them in method
    # 2 - pass departure aita in instead of having it as a class attribute
    #     defined in init
    def get_flights(
        self,
        departure_iata,
        destination_iata,
        departure_date,
        return_date,
        currency="GBP",
        min_nights=7,
        max_nights=28,
    ):
        """find flight information using Tequila Kiwi API and return a
        FlightData object

        Args:
            departure_iata (str): IATA Code for origin city
            destination_iata (str): IATA Code for destination city
            departure_date (str): dd/mm/YYYY for earliest departure
            return_date (str): dd/mm/YYYY for latest return
            currency (str, optional): currency to return. Defaults to "GBP".
            min_nights (int, optional): minimum nights. Defaults to 7.
            max_nights (int, optional): maximum nights. Defaults to 28.

        Returns:
            FlightData: FlightData for lowst cost flight
        """
        url = self.url_base + "/v2/search"
        params = {
            "fly_from": departure_iata,
            "fly_to": destination_iata,
            "date_from": departure_date,
            "date_to": return_date,
            "nights_in_dst_from": min_nights,
            "nights_in_dst_to": max_nights,
            "curr": currency,
            "flight_type": "round",
            "one_for_city": 1,
        }
        response = requests.get(url, params=params, headers=self.headers)
        data = response.json()
        if len(data["data"]) > 0:
            data = data["data"][0]
        else:
            return None

        flight_data = FlightData(
            departure_city=data["cityFrom"],
            departure_airport=data["flyFrom"],
            destination_city=data["cityTo"],
            destination_airport=data["flyTo"],
            departure_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][-1]["local_arrival"].split("T")[0],
            price=data["price"],
        )
        return flight_data

    def get_city_code(self, location):
        """Based on city name, return location code for first result from
        Tequila Kiwi locations query API

        Args:
            location (str): City Name

        Returns:
            str: IATA Code
        """
        url = self.url_base + "/locations/query"
        params = {"term": location, "location_types": "city", "limit": 1}
        result = requests.get(url, params=params, headers=self.headers)
        locations = result.json()
        return locations["locations"][0]["code"]
