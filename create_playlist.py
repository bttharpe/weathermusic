import os
import requests

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())



SPOTIFY_CREATE_PLAYLIST_URL = "https://api.spotify.com/v1/users/tyroget/playlists"
ACCESS_TOKEN = {access_token}

def create_new_playlist(name,public):
    response = requests.post(
        SPOTIFY_CREATE_PLAYLIST_URL,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
        json={
            "name": name,
            "public": public
        }
    )
    json_resp = response.json()
        
    return json_resp

def main():
    playlist = create_new_playlist(
        name="My Private Playlist",
        public=False
    )

    print(f"Playlist: {playlist}")


if __name__ == '__main__':
    main()
