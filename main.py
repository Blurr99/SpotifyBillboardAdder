import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

ClientID = CLIENT_ID
ClientSecret = CLIENTSECRET

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id=ClientID,
        client_secret=ClientSecret,
        redirect_uri="http://example.com",
        show_dialog=True,
        cache_path="token.txt"
    )
)


user_id = sp.current_user()["id"]

# date = '2023-07-01'
date = input("Enter the date of your choice!(YYYY-MM-DD): ")

URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL)
spotify_web_page = response.text
soup = BeautifulSoup(spotify_web_page,"html.parser")

song_list = soup.select("li ul li h3")
songs = [song.getText().strip() for song in song_list]

song_uris = []


for song in songs:
    result = sp.search(q=f"track:{song} year:2000", type='track')
    try:
        uri = result["tracks"]["items"][0]["uri"]
        # print(uri)
        song_uris.append(uri)
    except IndexError:
        # print(uri)
        print(f"{song} doesn't exist in Spotify. Skipped.")

# print(song_uris)

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", collaborative=False , public=False)
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist['id'], tracks=song_uris)



