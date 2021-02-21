import spotipy
from spotipy.oauth2 import SpotifyOAuth

from dotenv import load_dotenv

from song import Song

load_dotenv()


class Spotify:
    def __init__(self):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(scope="playlist-modify-private")
        )
        self.user = self.sp.current_user()

    def add_songs_to_playlist(self, song_list):
        tracks = self.get_track_uri_list(song_list)
        self.sp.user_playlist_add_tracks(
            user=self.user["id"],
            playlist_id=self.playlist["id"],
            tracks=tracks,
        )

    def create_playlist(
        self, name, public=False, description=None, song_list=None
    ):
        self.playlist = self.sp.user_playlist_create(
            user=self.user["id"],
            name=name,
            public=public,
            description=description,
        )
        if song_list:
            self.add_songs_to_playlist(song_list)

    def get_track_uri_list(self, song_list):
        tracks = []
        for song in song_list:
            uri = self._get_spotify_uri(song)
            if uri:
                tracks.append(uri)
        return tracks

    def _get_spotify_uri(self, song: Song):
        title = song.title
        artist = song.artist
        results = self.sp.search(
            q=f"track:{title} artist:{artist}",
            type="track",
            limit=1,
        )
        if len(results["tracks"]["items"]) > 0:
            return results["tracks"]["items"][0]["uri"]
        else:
            if "Featuring" in artist:
                artist = artist.split(" Featuring")[0]
                return self._get_spotify_uri(Song(title, artist))
            elif "&" in artist:
                artist = artist.split(" &")[0]
                return self._get_spotify_uri(Song(title, artist))
            elif " x " in artist.lower():
                artist = artist.lower().split(" x ")[0]
                return self._get_spotify_uri(Song(title, artist))
            else:
                print(f"{title} by {artist} not found")
                return None
