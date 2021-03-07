import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    def __init__(self):
        self.chrome_driver_path = "/usr/bin/chromedriver"
        self.ig_user = os.getenv("IG-USER")
        self.ig_pass = os.getenv("IG-PASS")
        self.target_account = os.getenv("TARGET-ACCOUNT")


config = Config()
