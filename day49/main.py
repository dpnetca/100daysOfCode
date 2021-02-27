import os
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from dotenv import load_dotenv

load_dotenv()

chrome_driver = "/usr/bin/chromedriver"

search_url = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&keywords="
keywords = "ccie"
url = search_url + keywords

driver = webdriver.Chrome(chrome_driver)

driver.get(url)

time.sleep(2)
# SIGN IN
driver.find_element_by_link_text("Sign in").click()

time.sleep(2)

username = driver.find_element_by_id("username")
username.send_keys(os.getenv("LI_USERNAME"))

password = driver.find_element_by_id("password")
password.send_keys(os.getenv("LI_PASSWORD"))

submit = driver.find_element_by_css_selector("button[type='submit']")
submit.click()

time.sleep(2)

driver.find_element_by_css_selector(
    "li-icon[type='chevron-down-icon']"
).click()
time.sleep(1)
job_list = driver.find_elements_by_class_name("job-card-container")

# find the first job that allows to submit with just a phone number
for job in job_list:
    job.click()
    time.sleep(1)
    driver.find_element_by_class_name("jobs-apply-button").click()

    # Look for Submit Application Button, if not found then this is a
    # multi input applicationh and we want to skip those
    # could also get button and check if it is submit or next w/ if
    # statement instead of using a try/except
    try:
        submit_application = driver.find_element_by_css_selector(
            "button[aria-label='Submit application']"
        )
        # if found break the loop we only want to find first job not all
        break
    except NoSuchElementException:
        pass

    # if this job was multi-step then discard job and repeat loop with next
    # job
    driver.find_element_by_css_selector("li-icon[type='cancel-icon']").click()
    time.sleep(1)

    driver.find_element_by_css_selector(
        ".artdeco-modal__confirm-dialog-btn.artdeco-button--primary"
    ).click()
    time.sleep(1)

phone = driver.find_element_by_class_name("fb-single-line-text__input")
phone.send_keys(os.getenv("LI_PHONE_NUMBER"))

# uncomment the following line to submit the application: (not tested)
# submit_application.click()

# driver.quit()
