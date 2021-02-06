import os
import smtplib
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

# MY_LAT = 51.507351  # Your latitude
# MY_LONG = -0.127758  # Your longitude
# TZ_OFFSET = ...

MY_LAT = os.getenv("MY_LAT")
MY_LONG = os.getenv("MY_LONG")
TZ_OFFSET = os.getenv("TZ_OFFSET")


# Your position is within +5 or -5 degrees of the ISS position.
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # uncomment to hard code for testing
    # iss_latitude = MY_LAT + 3
    # iss_longitude = MY_LONG + 3

    if (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    ):
        return True
    return False


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters
    )
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour - TZ_OFFSET

    # uncomment to hard code for testing
    # time_now = 23

    if time_now > sunset or time_now < sunrise:
        return True
    return False


def send_mail():
    my_email = os.getenv("MY_EMAIL")
    email_password = os.getenv("EMAIL_PASSWORD")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = os.getenv("SMTP_PORT", 25)

    message = (
        f"To:{my_email}\n"
        f"From:{my_email}\n"
        "Subject:Look Up\n\n"
        "Look up to see ISS"
    )

    with smtplib.SMTP(smtp_server, port=smtp_port) as connection:
        # connection.starttls()
        connection.login(user=my_email, password=email_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=message,
        )


if is_iss_overhead() and is_dark():
    send_mail()

# BONUS: run the code every 60 seconds.
# cron job FTW...or python anywhere...or leave code running in background
# with a loop and time.sleep(60) ....
