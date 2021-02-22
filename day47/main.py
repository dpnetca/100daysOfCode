#!/usr/bin/env python
import os
import smtplib
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://www.amazon.ca/gp/product"


def get_item_price(item_id):
    url = f"{BASE_URL}/{item_id}"
    headers = {
        "Accept-Language": "en-US,en;q=0.9",
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 "
            "Safari/537.36 Edg/88.0.705.74"
        ),
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    price_block = soup.find(name="span", id="priceblock_ourprice")
    price_block = price_block.get_text()
    price = float(price_block.split("\xa0")[1])

    return price


def send_email(
    message,
    sender=os.getenv("EMAIL_ADDRESS"),
    email_password=os.getenv("EMAIL_PASSWORD"),
    recipient=os.getenv("EMAIL_ADDRESS"),
    subject="Amazon Price Alert",
):

    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = os.getenv("SMTP_PORT", "25")
    with smtplib.SMTP(host=smtp_host, port=smtp_port) as smtp:
        smtp.login(user=sender, password=email_password)
        smtp.sendmail(
            from_addr=sender,
            to_addrs=recipient,
            msg=(
                f"From:{sender}\n"
                f"To:{recipient}\n"
                f"Subject:{subject}\n\n"
                f"{message}"
            ),
        )


items = [
    {
        "id": "B078MGXLVS",
        "threshold_price": 70.00,  # normal price 69.99
        "description": "Blue Radius III Custom Shockmount",
    },
]

for item in items:
    price = get_item_price(item["id"])
    if price <= item["threshold_price"]:
        message = (
            f"{item['description']} is priced at ${price:.2f}, which is below "
            f"our threshold of ${item['threshold_price']:.2f}\n"
            f"URL: {BASE_URL}/{item['id']}"
        )
        send_email(message=message)
