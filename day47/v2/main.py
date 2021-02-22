#!/usr/bin/env python
from amazon_price_checker import AmazonPriceChecker
from notification_manager import NotificationManager
from item_info import ItemInfo


notification = NotificationManager()
apc = AmazonPriceChecker()
apc.add_item(
    ItemInfo(
        item_id="B078MGXLVS",
        threshold_price=70.00,  # normal price = 69.99
        description="Blue Radius III Custom Shockmount",
    )
)
apc.add_item(
    ItemInfo(
        item_id="B078MLBGRM",
        threshold_price=140.00,  # normal price = 139.00
        description="Blue Compass Premium Tube-Style Broadcast Boom Arm",
    )
)
apc.get_all_item_price()

cheap_items = apc.get_cheap_items()

for item in cheap_items:
    message = (
        f"{item.description} is priced at ${item.actual_price:.2f}, "
        f"which is below our threshold of ${item.threshold_price:.2f}\n"
        f"URL: {item.url}"
    )
    notification.send_email(message=message)
