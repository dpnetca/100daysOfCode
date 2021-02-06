import requests
from datetime import datetime

MY_LAT = 50.445210
MY_LNG = -104.618896
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()

# # print(data)
# # print(data["iss_position"])

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (latitude, longitude)
# print(iss_position)

parameters = {"lat": MY_LAT, "lng": MY_LNG, "formatted": 0}

response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters
)

data = response.json()
# Parse our the hour in returned results
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now.hour)

# there is a bug in course logic...sunrise/sunset returns time in UTC,
# datetime giving time in local timezone
