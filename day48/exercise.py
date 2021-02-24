#!/usr/bin/env python
from selenium import webdriver

chrome_driver_path = "/usr/bin/chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

# driver.get("https://www.amazon.ca/gp/product/B078MGXLVS")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)


driver.get("https://python.org")
# search_box = driver.find_element_by_name("q")
# print(search_box.tag_name)
# print(search_box.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)
# doc_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(doc_link.text)

# From web browser inspect element the right click -> copy -> copy xpath
# bug_link = driver.find_element_by_xpath(
#     '//*[@id="site-map"]/div[2]/div/ul/li[3]/a'
# )
# print(bug_link.text)
# print(bug_link.get_attribute("href"))


# all_li_links = driver.find_elements_by_css_selector("li a")
# for link in all_li_links:
#     print(link.get_attribute("href"))

# Challenge 1
# python.org has an upcoming events section that looks like this:
# Upcoming Events
# 2021-02-24 Careers with Python: Volume 0
# 2021-03-13 PyCon Belarus 2021
# 2021-03-18 PyCon Cameroon 2021
# 2021-03-22 Python Web Conference 2021
# 2021-03-25 An introduction to delivering technical presentations with
#            confidence - PyLadies Amsterdam
# scrape these elements into a dictionary that has an index # with a
# nested dictionary containing the date and name of the event

# .menu not needed in times
# li also works instead of .menu for event name
event_times = driver.find_elements_by_css_selector(".event-widget .menu time")
event_names = driver.find_elements_by_css_selector(".event-widget .menu a")


events = {}
for idx, event in enumerate(event_times):
    events[idx] = {
        "time": event.text,
        "name": event_names[idx].text,
    }

# could also do dict comprehension:
# events = {
#     idx: {
#         "time": event.text,
#         "name": event_names[idx].text,
#     }
#     for idx, event in enumerate(event_times)
# }

print(events)

# driver.close()  # close open tab
driver.quit()  # close entire browser
