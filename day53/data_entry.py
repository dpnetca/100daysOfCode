import time

from selenium import webdriver

from property_detail import PropertyDetail
from config import config


class DataEntry:
    def __init__(self, url) -> None:
        self.url = url
        self.driver = webdriver.Chrome(config.chrome_driver)

    def complete_form(self, prop: PropertyDetail) -> None:
        self.driver.get(self.url)
        time.sleep(1)
        inputs = self.driver.find_elements_by_css_selector(
            "input[type='text']"
        )
        inputs[0].send_keys(prop.address)
        inputs[1].send_keys(prop.price)
        inputs[2].send_keys(prop.zillow_link)
        self.driver.find_element_by_css_selector("span .exportLabel").click()

    def input_list(self, property_list) -> None:
        for p in property_list:
            self.complete_form(p)
            time.sleep(0.5)

    def quit(self):
        time.sleep(2)
        self.driver.quit()
