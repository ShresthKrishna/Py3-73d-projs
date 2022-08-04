from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

SPOTIFY_ID = "e0ec86aae95f45e5bda5bee2df6e5744"
SPOTIFY_CLIENT = "636c5122c46a4f16aca4220832b8f33c"
SPOTIFY_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_URI = "http://example.com"
SPOTIFY_AUTH = "http://example.com/?code=AQCdx3sbFjeq18vETlYYHpXdCZO8i3Bhn8KPaotOlZRC1xyl8lQzYC9lOsZe2QIwQnw79sFZfityGjuX9sdlR52Mfw6w-_DpQyRcrtXgQsDeAq7X911-ix6tYa_DfyW9e_U9Pn-Da6Pi9kBJuqeGjNicnhpQ_pbzxnPXDTOM1vM3-7jYoYYZYtqi36MSkwk"

year = input("Which year song u want in format(YYYY-MM-DD): ")
URL = f"https://www.billboard.com/charts/hot-100/{year}"
response = requests.get(URL)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                    client_id="e0ec86aae95f45e5bda5bee2df6e5744",
                    client_secret="636c5122c46a4f16aca4220832b8f33c",
                    redirect_uri="http://example.com",
                    scope="playlist-modify-private",
                    show_dialog=True,
                    cache_path="token.txt"
                    ))
userid = sp.current_user()["id"]


# print(response.text)
soup = BeautifulSoup(response.text,"html.parser")
# print(soup.prettify())
song = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
song_list = [song.getText() for song in song]
print(song_list)
year_1 = year.split("-")[0]
uri_list = []

for j in song_list:
    results = sp.search(q=f"track:{j} year:{year_1}", type="track")
    print(results)
    try:
        uri = results["tracks"]["items"][0]["uri"]
        uri_list.append(uri)
    except IndexError:
        print(f"{j} not in Spotify, Skipped.")
playlist = sp.user_playlist_create(user=userid, name=f"{year} Billboard 100", public=False)
print(playlist)
sp.playlist_add_items(playlist['id'], items=uri_list)