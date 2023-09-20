from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QDialog
from PySide6.QtWebEngineWidgets import QWebEngineView
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from gui.ui_spotify import Ui_Spotify


class SpotifyForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Spotify()
        self.ui.setupUi(self)

        # Set the URL of the Spotify playlist embed
        # playlist_id = "6zwTfZcouUES8PNcniA4if"
        playlist_id = "37i9dQZF1DX5Ejj0EkURtP"
        url = f"https://open.spotify.com/embed/playlist/{playlist_id}?utm_source=generator&theme=0"

        self.ui.webEngineView.load(QUrl(url))

        # Create a QWebEngineView wid


"""

# Set up Spotify API credentials
client_id = "your_client_id"
client_secret = "your_client_secret"
redirect_uri = "your_redirect_uri"

# Create a Spotify client with authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope="user-library-read",
    )
)

# Retrieve the user's saved tracks
results = sp.current_user_saved_tracks()
for item in results["items"]:
    track = item["track"]
    print(track["name"], " - ", track["artists"][0]["name"])
    """
