from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import re


def is_valid_date_format(date_str):
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    return bool(re.match(pattern, date_str))


SPOTIPY_CLIENT_ID = os.environ.get("CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REDIRECT_URI = "http://example.com"

flag = False
while not flag:
    time = input("What year do you want to travel to?\nType the date in this format YYYY-MM-DD:\n")
    flag = is_valid_date_format(time)


response = requests.get(f"https://www.billboard.com/charts/hot-100/{time}/")
webpage_content = response.text

soup = BeautifulSoup(webpage_content, "html.parser")
# print(soup.prettify())

titles = soup.find_all("h3", {"id": "title-of-a-story"})

hot_100 = [title.text for title in titles]

formatted_hot_100 = []
for sub in hot_100:
    formatted_hot_100.append(sub.replace("\t", ""))

final_hot_100 = []

for sub in formatted_hot_100:
    final_hot_100.append(sub.replace("\n", ""))

song_names = final_hot_100[6::4]

print(song_names)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri=REDIRECT_URI,
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    show_dialog=True,
))

user_id = sp.current_user()["id"]

spotify_uris = []
for song_name in song_names:
    results = sp.search(q=song_name, limit=1, type='track')

    if results['tracks']['items']:
        # Extract the Spotify URI of the first search result
        spotify_uri = results['tracks']['items'][0]['uri']
        spotify_uris.append(spotify_uri)
    else:
        print(f"No Spotify track found for: {song_name}")

# Print the list of Spotify song URIs
print("Spotify song URIs:")
for uri in spotify_uris:
    print(uri)

playlist_name = f"{time} Billboard 100"
playlist_description = f"Top songs from Billboard 100 {time}"
playlist_id = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description=playlist_description)[
    'id']

batch_size = 50

# Add tracks to the playlist in batches
for i in range(0, len(spotify_uris), batch_size):
    batch = spotify_uris[i:i + batch_size]
    sp.playlist_add_items(playlist_id, batch)

print(f"Added {len(spotify_uris)} tracks to the playlist.")

print(f"Created playlist: {playlist_name} (ID: {playlist_id})")
