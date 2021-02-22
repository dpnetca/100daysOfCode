import requests
from bs4 import BeautifulSoup

from item_info import ItemInfo

BASE_URL = "https://www.amazon.ca/gp/product"


class AmazonPriceChecker:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url
        self.headers = {
            "Accept-Language": "en-US,en;q=0.9",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 "
                "Safari/537.36 Edg/88.0.705.74"
            ),
        }
        self.items = []

    def add_item(self, item: ItemInfo):
        item.url = f"{BASE_URL}/{item.item_id}"
        self.items.append(item)

    def get_item_price(self, item_id):
        url = f"{self.base_url}/{item_id}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        price_block = soup.find(name="span", id="priceblock_ourprice")
        price_block = price_block.get_text()
        price = float(price_block.split("\xa0")[1])

        return price

    def get_all_item_price(self):
        for item in self.items:
            item.actual_price = self.get_item_price(item.item_id)

    def get_cheap_items(self):
        return [item for item in self.items if item.is_below_threshold()]
