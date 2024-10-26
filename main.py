import yt_dlp
import os

DOWNLOAD_PATH = "Downloads"
# Enter your file destination you want to store the videos.

def download_youtube_playlist(playlist_url):
    ydl_opts = {
        'outtmpl': os.path.join(DOWNLOAD_PATH, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

if not os.path.exists(DOWNLOAD_PATH):
    os.makedirs(DOWNLOAD_PATH)

playlist_url = input("Enter the YouTube playlist URL: ")
download_youtube_playlist(playlist_url)
