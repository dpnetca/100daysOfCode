import time
import os

from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementClickInterceptedException,
)

from dotenv import load_dotenv

load_dotenv()

chrome_driver = "/usr/bin/chromedriver"

url = "https://tinder.com/"

driver = webdriver.Chrome(chrome_driver)

driver.get(url)

time.sleep(1)
# xpath for acccept cookies link
xpath = '//*[@id="t-1801132545"]/div/div[2]/div/div/div[1]/button/span'
# if the accept cookie link exists, click it
try:
    driver.find_element_by_xpath(xpath).click()
except NoSuchElementException:
    print("Cookie popup not found")

time.sleep(1)
# xpath for Log in button in top right of screen
xpath = (
    '//*[@id="t-1801132545"]/div/div[1]/div/main/div[1]/div/div/div/div/'
    "header/div/div[2]/div[2]/button/span"
)
driver.find_element_by_xpath(xpath).click()

time.sleep(1)
# xpath Log In with Facebook button
xpath = (
    '//*[@id="t--239073259"]/div/div/div[1]/div/div[3]/span/div[2]/'
    "button/span[2]"
)
driver.find_element_by_xpath(xpath).click()

time.sleep(1)
# switch to facebook login pop up and login with facebook details
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_id("email").send_keys(os.getenv("FB_USERNAME"))
driver.find_element_by_id("pass").send_keys(os.getenv("FB_PASSWORD"))
driver.find_element_by_id("loginbutton").click()

time.sleep(3)
# switch back to main tinder window
driver.switch_to.window(driver.window_handles[0])
# Allow tinder to use my location
xpath = '//*[@id="t--239073259"]/div/div/div/div/div[3]/button[1]/span'
try:
    driver.find_element_by_xpath(xpath).click()
except NoSuchElementException:
    print("location popup not found")


# Not Interested in Notifcations
time.sleep(2)
xpath = '//*[@id="t--239073259"]/div/div/div/div/div[3]/button[2]/span'
try:
    driver.find_element_by_xpath(xpath).click()
except NoSuchElementException:
    print("notification popup not found")

time.sleep(2)
# xpath for dislike button
xpath = (
    '//*[@id="t-1801132545"]/div/div[1]/div/main/div[1]/div/div/div[1]'
    "/div/div[2]/div[2]/button"
)
# try and click disklike in loop with pause between, print an error to
# console if dislike button not found
for _ in range(10):
    try:
        driver.find_element_by_xpath(xpath).click()
    except NoSuchElementException:
        print("dislike button not found")
    except ElementClickInterceptedException:
        print("click intercepted")
    time.sleep(2)

driver.quit()
