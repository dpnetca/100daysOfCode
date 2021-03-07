import time

from config import config
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(config.chrome_driver_path)
        self.ig_base_url = "https://www.instagram.com"

    def login(self):
        url = self.ig_base_url + "/accounts/login/"
        self.driver.get(url)
        time.sleep(1)
        username = self.driver.find_element_by_name("username")
        username.send_keys(config.ig_user)

        password = self.driver.find_element_by_name("password")
        password.send_keys(config.ig_pass)
        time.sleep(1)
        self.driver.find_element_by_css_selector(
            "button[type='submit']"
        ).click()
        time.sleep(2)

    def find_followers(self):
        url = self.ig_base_url + "/" + config.target_account
        self.driver.get(url)
        time.sleep(2)

        self.driver.find_element_by_css_selector(
            f'a[href="/{config.target_account}/followers/"]'
        ).click()

        time.sleep(2)
        popup = self.driver.find_element_by_class_name("isgrP")

        # scroll down 10 times
        for _ in range(10):
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", popup
            )
            time.sleep(0.5)
        time.sleep(1)

    def follow(self):
        dialog_buttons = self.driver.find_elements_by_css_selector(
            "div[role='dialog'] li button[type='button']"
        )
        for button in dialog_buttons:
            try:
                button.click()
            except ElementClickInterceptedException:
                profile_buttons = self.driver.find_elements_by_css_selector(
                    "div[role='dialog'] button"
                )
                for profile_button in profile_buttons:
                    if profile_button.text == "Cancel":
                        profile_button.click()
                        time.sleep(1)
                        break
                button.click()
            time.sleep(1)

        time.sleep(5)

    def quit(self):
        self.driver.quit()
