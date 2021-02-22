class ItemInfo:
    item_id: str
    threshold_price: float
    description: str
    actual_price: float
    url: str

    def __init__(
        self, item_id, threshold_price, description, url=None, actual_price=-1
    ):
        self.item_id = item_id
        self.threshold_price = threshold_price
        self.description = description
        self.actual_price = actual_price
        self.url = url

    def is_below_threshold(self):
        if self.actual_price >= 0:
            return self.actual_price <= self.threshold_price
        return False
