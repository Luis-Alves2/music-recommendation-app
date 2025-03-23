import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="user-top-read playlist-read-private"
))

def get_user_top_tracks():
    """Fetch current user's top tracks."""
    results = sp.current_user_top_tracks(limit=10)
    return results

# Test the function
if __name__ == "__main__":
    tracks = get_user_top_tracks()
    print(tracks)