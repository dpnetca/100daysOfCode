import os
import time

from selenium import webdriver

GOOD_PCT = 0.9
ACCEPTABLE_PCT = 0.5
ISP = "not my real ISP"


class InternetSpeedTwitterBot:
    def __init__(
        self,
        driver_path=os.getenv("CHROME_DRIVER_PATH", "/usr/bin/chromedriver"),
        expected_up=int(os.getenv("EXPECTED_UP", 75)),
        expected_down=int(os.getenv("EXPECTED_DOWN", 150)),
    ):
        self.driver = webdriver.Chrome(driver_path)
        self.expected_up = expected_up
        self.expected_down = expected_down
        self.tweet = None

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(1)
        self.driver.find_element_by_class_name("start-text").click()

        # check overall-progress, if complete break loop, if not, wait
        # 2 seconds and try again up to a maximum of 120 seconds
        for _ in range(60):
            progress = self.driver.find_element_by_class_name(
                "overall-progress"
            ).text
            if progress.startswith("Your speed test has completed"):
                break
            time.sleep(2)

        download_speed_tag = self.driver.find_element_by_class_name(
            "download-speed"
        )
        self.actual_down = float(download_speed_tag.text)

        upload_speed_tag = self.driver.find_element_by_class_name(
            "upload-speed"
        )
        self.actual_up = float(upload_speed_tag.text)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(2)
        username = self.driver.find_element_by_name(
            "session[username_or_email]"
        )
        username.send_keys(os.getenv("TWITTER_EMAIL"))

        password = self.driver.find_element_by_name("session[password]")
        password.send_keys(os.getenv("TWITTER_PASSWORD"))

        self.driver.find_element_by_css_selector(
            'div[data-testid="LoginForm_Login_Button"]'
        ).click()

        time.sleep(2)
        tweet_text = self.driver.find_element_by_css_selector(
            'div[data-testid="tweetTextarea_0"]'
        )

        if not self.tweet:
            self._compose_tweet()

        tweet_text.send_keys(self.tweet)

        send_tweet = self.driver.find_element_by_css_selector(
            'div[data-testid="tweetButtonInline"]'
        )
        send_tweet.click()

    def _compose_tweet(self):
        down_pct = self.actual_down / self.expected_down
        up_pct = self.actual_up / self.expected_up
        self.tweet = (
            "Expected Internet Speed: "
            f"{self.expected_down} down / {self.expected_up} up.\n"
            "Actual Internet Speed: "
            f"{self.actual_down} down / {self.actual_up} up.\n"
        )
        if down_pct >= GOOD_PCT and up_pct >= GOOD_PCT:
            self.tweet += f"Thats pretty good.  Thanks {ISP}"
        elif down_pct >= ACCEPTABLE_PCT and up_pct >= ACCEPTABLE_PCT:
            self.tweet += f"C'mon {ISP}, you can do better"
        else:
            self.tweet += f"{ISP} what the heck, this is awful!!"
