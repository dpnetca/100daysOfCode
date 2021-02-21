import requests
from bs4 import BeautifulSoup

from song import Song

BASE_URL = "https://www.billboard.com/charts/hot-100"


class Top100:
    def __init__(self, date_in=None):
        self.top_100 = self.get_top_100(date_in)

    @classmethod
    def get_top_100(cls, date_in=None):
        if date_in:
            endpoint = f"/{date_in}"
        else:
            endpoint = ""

        url = BASE_URL + endpoint

        response = requests.get(url)
        response.raise_for_status()

        return cls._parse_top_100(response.text)

    @staticmethod
    def _parse_top_100(text):
        soup = BeautifulSoup(text, "html.parser")

        chart_rows = soup.find_all(
            name="span",
            class_="chart-element__information",
        )

        song_list = []
        for chart_row in chart_rows:
            title = chart_row.find(
                name="span", class_="chart-element__information__song"
            ).get_text(strip=True)
            artist = chart_row.find(
                name="span", class_="chart-element__information__artist"
            ).get_text(strip=True)
            song = Song(title, artist)
            song_list.append(song)
        return song_list
