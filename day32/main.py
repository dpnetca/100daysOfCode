import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
my_email = os.getenv("MY_EMAIL")
email_password = os.getenv("EMAIL_PASSWORD")
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = os.getenv("SMTP_PORT", 25)


with smtplib.SMTP(smtp_server, port=smtp_port) as connection:
    # connection.starttls()
    connection.login(user=my_email, password=email_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="100days@dpnet.ca",
        msg="Subject:Hello\n\nThis the body of my email",
    )
