import os
from twilio.rest import Client


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

    def send_flight_alert_sms(self, flight):
        """Generate a sms message based on passed in Flight Data and send SMS

        Args:
            flight (FlightData): flight data
        """
        message = (
            f"Low Price Alert! Only ${flight.price} to fly from "
            f"{flight.departure_city}-{flight.departure_airport} to "
            f"{flight.destination_city}-{flight.destination_airport}, from "
            f"{flight.departure_date} to {flight.return_date}."
        )
        self.send_sms(message)
