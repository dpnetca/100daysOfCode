import os
from twilio.rest import Client
import smtplib
from dotenv import load_dotenv

load_dotenv()


class NotificationManager:
    # This class is responsible for sending notifications with the deal
    # flight details.
    def __init__(self):
        self.client = Client(
            os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN")
        )
        self.twilio_number = os.getenv("TWILIO_NUMBER")
        self.my_cell = os.getenv("MY_CELL")

    def send_sms(self, message):
        """send SMS message via Twilio
        Args:
            message (string): Message to send
        """
        self.client.messages.create(
            body=message,
            from_=self.twilio_number,
            to=self.my_cell,
        )

    def send_email(self, message, email):
        from_email = os.getenv("MY_EMAIL")
        with smtplib.SMTP(
            os.getenv("SMTP_SERVER"), port=os.getenv("SMTP_PORT", 25)
        ) as connection:
            # connection.starttls()
            connection.login(
                user=from_email, password=os.getenv("EMAIL_PASSWORD")
            )
            connection.sendmail(
                from_addr=from_email,
                to_addrs=email,
                msg=(
                    f"From:{from_email}\n"
                    f"To:{email}\n"
                    f"Subject:Flight Deal\n\n"
                    f"{message}"
                ),
            )

    def send_flight_alert_sms(self, flight):
        """Generate a sms message based on passed in Flight Data and send SMS

        Args:
            flight (FlightData): flight data
        """
        message = self.prepare_message(flight)
        self.send_sms(message)

    def send_flight_alert_email(self, flight, email):
        """Generate a message based on passed in Flight Data and send Email

        Args:
            flight (FlightData): flight data
        """
        message = self.prepare_message(flight)
        message += (
            f"\n\nLink: https://www.google.com/flights/?hl=en#flt="
            f"{flight.departure_airport}.{flight.destination_airport}."
            f"{flight.departure_date}*"
            f"{flight.destination_airport}.{flight.departure_airport}."
            f"{flight.return_date}"
        )
        self.send_email(message, email)

    def prepare_message(self, flight):
        message = (
            f"Low Price Alert! Only ${flight.price} to fly from "
            f"{flight.departure_city}-{flight.departure_airport} to "
            f"{flight.destination_city}-{flight.destination_airport}, from "
            f"{flight.departure_date} to {flight.return_date}."
        )
        if flight.stop_overs > 0:
            if flight.stop_overs == 1:
                stopover = "stop over"
            else:
                stopover = "stop overs"
            message += (
                f"Flight has {flight.stop_overs} {stopover}, "
                f"via {flight.via_city}"
            )
        return message
