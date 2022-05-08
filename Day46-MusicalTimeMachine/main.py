from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "YOUR SPOTIFY APP CLIENT ID"
CLIENT_SECRET = "YOUR SPOTIFY APP CLIENT SECRET"

date = input("Which year you want to travel to? Enter the date in the format YYYY-MM-DD:")

URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url=URL)
website_html = response.text
soup = BeautifulSoup(website_html, 'html.parser')
song_titles = [song.getText().replace("\n", "").replace("\t", "") for song in soup.select("li h3")]
song_names = song_titles[:100]

sp = spotipy.Spotify(
    oauth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://example.com",
        scope="playlist-modify-private",
        cache_path='token.txt',
        show_dialog=True
    )
)

user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type='track')
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"The {song} doesn't exist on spotify....Skipped!!!")

playlist = sp.user_playlist_create(name=f"{date} Billboard 100", public=False, user=user_id)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
