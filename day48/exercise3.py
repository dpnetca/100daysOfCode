#!/usr/bin/env python

from selenium import webdriver

chrome_driver_path = "/usr/bin/chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element_by_name("fName")
lname = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
submit = driver.find_element_by_css_selector("button[type='submit']")
# instructor method:
# submit = driver.find_element_by_css_selector("form button")

fname.send_keys("Denis")
lname.send_keys("Pointer")
email.send_keys("fake@fake.ca")
submit.click()

driver.quit()
