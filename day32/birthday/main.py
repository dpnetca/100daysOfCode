#!/usr/bin/env python
# #################### Extra Hard Starting Project #####################

import smtplib
import random
import os
import pandas as pd
import datetime as dt
from dotenv import load_dotenv

load_dotenv()

LETTERS = [
    "letter_templates/letter_1.txt",
    "letter_templates/letter_2.txt",
    "letter_templates/letter_3.txt",
]

birthday_file = "birthdays.csv"


def create_letter(name):
    letter_file = random.choice(LETTERS)
    with open(letter_file) as f:
        letter = f.read()
    letter = letter.replace("[NAME]", name.strip())
    return letter


def send_letter(email, letter):
    my_email = os.getenv("MY_EMAIL")
    email_password = os.getenv("EMAIL_PASSWORD")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = os.getenv("SMTP_PORT", 25)

    with smtplib.SMTP(smtp_server, port=smtp_port) as connection:
        # connection.starttls()
        connection.login(user=my_email, password=email_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email.strip(),
            msg=f"Subject:Happy Birthday\n\n{letter}",
        )
        print(email)
        print(letter)


now = dt.datetime.now()
current_month = now.month
current_day = now.day

# 1. Update the birthdays.csv
df = pd.read_csv(birthday_file)

# 2. Check if today matches a birthday in the birthdays.csv
for i_, row in df.iterrows():
    birth_month = row["month"]
    birth_day = row["day"]

    # comment after watching solution:
    # Make a Tupple instead and compare tupples
    # birthday = (row["month"], row["day"]
    # today = (now.month, now.day)
    # if birthday == today":

    if birth_month == current_month and birth_day == current_day:

        # 3. If step 2 is true, pick a random letter from letter
        # templates and replace the [NAME] with the person's actual
        # name from birthdays.csv
        letter = create_letter(row["name"])

        # 4. Send the letter generated in step 3 to that person's email
        # address.
        send_letter(row["email"], letter)
