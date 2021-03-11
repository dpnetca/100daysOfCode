from typing import List
import re

from property_detail import PropertyDetail
import requests
from bs4 import BeautifulSoup


class PropertyFinder:
    def __init__(self, url) -> None:
        self.url = url
        self.property_list = []

    def get_property_list(self) -> List[PropertyDetail]:
        headers = {
            "Accept-Language": "en-US,en;q=0.9",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 "
                "Safari/537.36 Edg/88.0.705.74"
            ),
        }
        response = requests.get(self.url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        listings = soup.find_all(class_="list-card")
        for listing in listings:
            address = listing.find(name="address").get_text()
            address = address.split("|")[-1]

            price = listing.find(class_="list-card-price").get_text()
            price = re.split("/|\+| ", price)[0]

            zillow_link = listing.find(name="a").get("href")
            if "http" not in zillow_link:
                zillow_link = f"https://www.zillow.com/{zillow_link}"

            self.property_list.append(
                PropertyDetail(address, price, zillow_link)
            )
