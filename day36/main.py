#!/usr/bin/env python
"""
STEP 1: Use https://www.alphavantage.co
When STOCK price increase/decreases by 5% between yesterday and the day
before yesterday then print("Get News").
STEP 2: Use https://newsapi.org
Instead of printing ("Get News"), actually get the first 3 news pieces
for the COMPANY_NAME.
STEP 3: Use https://www.twilio.com
Send a seperate message with the percentage change and each article's title
and description to your phone number.


# Optional: Format the SMS message like this:

TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge
funds and prominent investors are required to file by the SEC The 13F
filings show the funds' and investors' portfolio positions as of March
31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge
funds and prominent investors are required to file by the SEC The 13F
filings show the funds' and investors' portfolio positions as of March
31st, near the height of the coronavirus market crash.
"""

import os
import requests
import datetime as dt
from twilio.rest import Client

from dotenv import load_dotenv

load_dotenv()

# STOCK = "TSLA"
# COMPANY_NAME = "Tesla Inc"
STOCK = os.getenv("STOCK", "GME")
COMPANY_NAME = os.getenv("COMPANY_NAME", "Gamestop")


def get_last_day(data, date):
    """parse the data to to find the last day of trading starting at
    given date and working backwards until trading data found, abort of no
    data found after 10 iterations

    Args:
        data (DICT): Dictionary of stock data from alphavantage.co
        date (datetime): datetime object to start search from

    Returns:
        tuple: (date, dict) where date is date of the data and the dict
        is the specific stock data for that date
    """

    # could use a while loop here, but if data is corrupted easy infinite
    # loop, use range of 10, can't imagine needing more then this....
    for _ in range(10):
        date_key = f"{date.year}-{date.month:02}-{date.day:02}"
        last_day = data.get(date_key)
        if last_day:
            return date, last_day
        date = date - dt.timedelta(days=1)


def get_previous_two_days(daily_time_series_data):
    """get stock data for last 2 days of trading

    Args:
        daily_time_series_data (dict): dictionary of stock data from
        alphavantage.co

    Returns:
        dict: dict with 2 days of stock data
    """
    date = dt.datetime.now()
    date, last_day_data = get_last_day(daily_time_series_data, date)
    date -= dt.timedelta(days=1)
    _, penultimate_day_data = get_last_day(daily_time_series_data, date)
    return {"last_day": last_day_data, "penultimate_day": penultimate_day_data}


def get_news():
    """User RESt API from newsapi to get headlines for defined company name

    Returns:
        list: list of returned articles
    """
    # could also use newsAPI client instead of API's direct...
    news_header = {"X-Api-Key": os.getenv("NEWS_API_KEY")}
    news_url = "https://newsapi.org/v2/everything"
    # news_params = {"q": COMPANY_NAME}
    news_params = {"qInTitle": COMPANY_NAME}
    news_response = requests.get(
        news_url, params=news_params, headers=news_header
    )
    data = news_response.json()
    return data["articles"]


def get_stocks():
    """get stock ticker data from alphavantage.co

    Returns:
        dict: dictionary of returned stock data
    """
    url = "https://www.alphavantage.co/query"
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": os.getenv("ALPHANTAGE_API_KEY"),
    }

    response = requests.get(url, params=parameters)
    data = response.json()
    return data["Time Series (Daily)"]


def send_sms(message):
    """send SMS message via Twilio

    Args:
        message (string): Message to send
    """
    client = Client(
        os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN")
    )
    sms = client.messages.create(
        body=message,
        from_=os.getenv("TWILIO_NUMBER"),
        to=os.getenv("MY_CELL"),
    )
    print(sms.status)


stock_data = get_stocks()
two_day_data = get_previous_two_days(stock_data)

last_close = float(two_day_data["last_day"]["4. close"])
penultimate_close = float(two_day_data["penultimate_day"]["4. close"])
percent_change = ((last_close - penultimate_close) / penultimate_close) * 100


if abs(percent_change) > 5:
    news = get_news()
    if len(news) >= 3:
        articles = 3
    else:
        articles = len(news)
    news = news[:articles]
    if percent_change > 0:
        icon = "🔺"
    else:
        icon = "🔻"
    for article in news:
        message = (
            f"{STOCK}: {icon} {abs(percent_change):.2f}%\n"
            f"Headline: {article['title']}\n"
            f"Brief: {article['description']}"
        )
        # print(message)
        send_sms(message)
