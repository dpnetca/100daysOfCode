import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    def __init__(self) -> None:
        self.chrome_driver = os.getenv("CHROME_DRIVER")
        self.zillow_url = os.getenv("ZILLOW_URL")
        self.google_form_url = os.getenv("GOOGLE_FORM_URL")


config = Config()
