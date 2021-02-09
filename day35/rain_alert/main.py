import os
import requests

from dotenv import load_dotenv
from twilio.rest import Client


def is_rain_forecast(hourly_forecast):
    """loop through an hourly forecast and return TRUE if rain is in the
    forecast

    Args:
        hourly_forecast (LIST): List of hourly forecasts from openweatherapi

    Returns:
        Bool: True if rain is forecast
    """
    for hour in hourly_forecast:
        for weather in hour["weather"]:
            if weather["id"] < 700:
                return True
    return False


load_dotenv()

url = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": os.getenv("LAT"),
    "lon": os.getenv("LON"),
    "exclude": "current,minutely,daily",
    "appid": os.getenv("OWN_API_KEY"),
}

result = requests.get(url, params=parameters)
result.raise_for_status()

data = result.json()
next_12_hours = data["hourly"][:12]

# if is_rain_forecast(next_12_hours):
# print("Bring an Umbrella")
# else:
#     print("No rain forecast")


if is_rain_forecast(next_12_hours):
    client = Client(
        os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN")
    )
    message = client.messages.create(
        body="Bring an Umbrella",
        from_=os.getenv("TWILIO_NUMBER"),
        to=os.getenv("MY_CELL"),
    )
    print(message.status)
