#!/usr/bin/env python
from dotenv import load_dotenv

from twitter_speed_bot import InternetSpeedTwitterBot

load_dotenv()

twitter_bot = InternetSpeedTwitterBot()

twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()
