import os
import smtplib

from dotenv import load_dotenv

load_dotenv()


class NotificationManager:
    def __init__(
        self,
        sender=os.getenv("EMAIL_ADDRESS"),
        email_password=os.getenv("EMAIL_PASSWORD"),
        recipient=os.getenv("EMAIL_ADDRESS"),
    ):
        self.sender = sender
        self.email_password = email_password
        self.recipient = recipient
        self.smtp_host = os.getenv("SMTP_HOST")
        self.smtp_port = os.getenv("SMTP_PORT", "25")

    def send_email(
        self,
        message,
        subject="Amazon Price Alert",
    ):
        with smtplib.SMTP(host=self.smtp_host, port=self.smtp_port) as smtp:
            smtp.login(user=self.sender, password=self.email_password)
            smtp.sendmail(
                from_addr=self.sender,
                to_addrs=self.recipient,
                msg=(
                    f"From:{self.sender}\n"
                    f"To:{self.recipient}\n"
                    f"Subject:{subject}\n\n"
                    f"{message}"
                ),
            )
