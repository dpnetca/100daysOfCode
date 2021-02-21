#!/usr/bin/env python
import requests

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from bs4 import BeautifulSoup
from dotenv import load_dotenv


def get_spotify_uri(sp, song):
    title = song["title"]
    artist = song["artist"]
    results = sp.search(
        q=f"track:{title} artist:{artist}",
        type="track",
        limit=1,
    )
    if len(results["tracks"]["items"]) > 0:
        return results["tracks"]["items"][0]["uri"]
    else:
        if "Featuring" in artist:
            artist = artist.split(" Featuring")[0]
            return get_spotify_uri(sp, {"title": title, "artist": artist})
        elif "&" in artist:
            artist = artist.split(" &")[0]
            return get_spotify_uri(sp, {"title": title, "artist": artist})
        elif " x " in artist.lower():
            artist = artist.lower().split(" x ")[0]
            return get_spotify_uri(sp, {"title": title, "artist": artist})
        else:
            print(f"{title} by {artist} not found")
            return None


load_dotenv()

BASE_URL = "https://www.billboard.com/charts/hot-100"

date_in = input(
    "Which year do you want to travel to? "
    "Type the date in this format: YYYY-MM-DD: "
)

url = BASE_URL + f"/{date_in}"
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

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

    song_list.append({"title": title, "artist": artist})


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(scope="playlist-modify-private")
)

user = sp.current_user()
playlist = sp.user_playlist_create(
    user=user["id"],
    name=f"{date_in} Billboard Top 100",
    public=False,
    description="100DaysofCode created playlist",
)

tracks = []
for song in song_list:
    uri = get_spotify_uri(sp, song)
    if uri:
        tracks.append(uri)

sp.user_playlist_add_tracks(
    user=user["id"], playlist_id=playlist["id"], tracks=tracks
)
