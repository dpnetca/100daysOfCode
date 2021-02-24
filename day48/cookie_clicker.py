#!/usr/bin/env python
import time
from selenium import webdriver

# URL = "http://orteil.dashnet.org/experiments/cookie/"
URL = "https://orteil.dashnet.org/cookieclicker/"
RUNTIME = 60 * 5
UPGRADE_TIMER = 5


def get_total_cookies(driver):
    cookies = driver.find_element_by_id("cookies")
    split_cookies = cookies.text.split(" ")
    return int(split_cookies[0].replace(",", ""))


def get_cookies_per_second(driver):
    cookies = driver.find_element_by_id("cookies")
    split_cookies = cookies.text.split(" ")
    return int(split_cookies[-1].replace(",", ""))


def get_items_prices(driver):
    prices = driver.find_elements_by_css_selector(
        ".storeSection .unlocked .price"
    )
    price_dict = dict()
    for idx, price in enumerate(prices):
        if price.text != "":
            price_dict[idx] = int(price.text.replace(",", ""))
    return price_dict


def buy_upgrades(driver):
    prices = get_items_prices(driver)
    for product_id, price in reversed(prices.items()):
        total_cookies = get_total_cookies(driver)
        if total_cookies > price:
            driver.find_element_by_id(f"product{product_id}").click()
            return True
    return False


chrome_driver_path = "/usr/bin/chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

driver.get(URL)

big_cookie = driver.find_element_by_id("bigCookie")

program_timeout = time.time() + RUNTIME
upgrade_timeout = time.time() + UPGRADE_TIMER
while time.time() < program_timeout:
    if time.time() > upgrade_timeout:
        upgrade_timeout = time.time() + UPGRADE_TIMER
        more_upgrades = True
        while more_upgrades:
            more_upgrades = buy_upgrades(driver)

    big_cookie.click()

print(f"Cookies/second: {get_cookies_per_second(driver)}")

driver.quit()
