#!/usr/bin/env python
from top100 import Top100
from spotify import Spotify


date_in = input(
    "Which year do you want to travel to? "
    "Type the date in this format: YYYY-MM-DD: "
)

song_list = Top100(date_in)

spotify = Spotify()
spotify.create_playlist(
    name=f"{date_in} Billboard Top 100ish",
    description="100DaysofCode created playlist",
    song_list=song_list.top_100,
)
