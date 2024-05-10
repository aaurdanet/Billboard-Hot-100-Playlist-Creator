# Billboard Hot 100 Playlist Creator

This script lets you travel back in time through music. The created Spotify playlist contains the top songs from the Billboard Hot 100 chart for a specific date, allowing you to relive the iconic hits that defined that period. Let the power of music transport you through time and space as you listen to the timeless classics and chart-topping favorites of yesteryears.

Prerequisites

Before running the script, make sure you have the following:

    Python 3 is installed on your system.
    The following Python libraries installed: beautifulsoup4, requests, and spotipy. You can install them using pip:

    pip install beautifulsoup4 requests spotipy

    A Spotify account.
    A Spotify Developer account to obtain CLIENT_ID and CLIENT_SECRET. 
    Set up environment variables for CLIENT_ID and CLIENT_SECRET in your system.

Usage

    Clone this repository or download the script file (main.py) to your local machine.

    Open a terminal or command prompt and navigate to the directory where the script is located.

    Run the script using the following command:

    python main.py

    You will be prompted to enter the date in the format YYYY-MM-DD for which you want to create the playlist.

    The script will then fetch the Billboard Hot 100 chart for the specified date and create a Spotify playlist with the top songs from that chart.

    Once the playlist is created, the script will print the Spotify URIs of the songs added to the playlist and provide the ID of the created playlist.

    You can access the created playlist on Spotify under your account.

Notes

    Make sure your Spotify account has sufficient permissions to create and modify playlists.
    Due to limitations in the Spotify API, not all songs from the Billboard Hot 100 may be available on Spotify. The script will skip any songs that cannot be found on Spotify.
    The created playlist will be set to private by default. You can modify the privacy settings later on the Spotify app or website.
