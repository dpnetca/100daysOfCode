#!/usr/bin/env python

import os
from datetime import datetime, timedelta

from dotenv import load_dotenv

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

load_dotenv()
CURRENCY = "GBP"
home_city_iata = os.getenv("HOME_CITY_IATA")

# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
data_manager = DataManager()
flight_search = FlightSearch()
notification = NotificationManager()

data_manager.get_destinations()
data_manager.get_users()

date_from = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
date_to = (datetime.now() + timedelta(days=(6 * 30))).strftime("%d/%m/%Y")

for row in data_manager.destination_data:
    if not row["iataCode"]:
        row["iataCode"] = flight_search.get_city_code(row["city"])
        data_manager.update_iata(row["id"], row["iataCode"])

    flight = flight_search.get_flights(
        departure_iata=home_city_iata,
        destination_iata=row["iataCode"],
        departure_date=date_from,
        return_date=date_to,
        currency=CURRENCY,
    )
    if flight and flight.price <= row["lowestPrice"]:
        for user in data_manager.user_data:
            notification.send_flight_alert_email(flight, user["email"])
