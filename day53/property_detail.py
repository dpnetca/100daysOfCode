class PropertyDetail:
    def __init__(self, address: str, price: str, zillow_link: str) -> None:
        self.address = address
        self.price = price
        self.zillow_link = zillow_link

    def __str__(self):
        return f"{self.address} for {self.price}. link: {self.zillow_link}"
