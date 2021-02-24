#!/usr/bin/env python
"""
Challenge #2

from wikipiedia main page get the number of articles
At top of page will be seomthing like:
    the free encyclopedia that anyone can edit.
    6,256,486 articles in English
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/usr/bin/chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")


# # instructor solution
# # there are 2 a tags in this div but this will match the first one
# # count = driver.find_element_by_css_selector("#articlecount a")

# count = driver.find_element_by_css_selector("a[title='Special:Statistics']")
# print(count.text)

# # count.click() # to click on link

# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

# how to type into a field
search = driver.find_element_by_name("search")
search.send_keys("python")
search.send_keys(Keys.ENTER)


driver.quit()
