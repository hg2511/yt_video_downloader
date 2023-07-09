import os
from pytube import YouTube, Playlist

FULL_PATH = os.path.abspath(".")
PLAYLIST_URL = input("Enter the playlist link : ")
playlist = Playlist(PLAYLIST_URL)

path = os.path.join(FULL_PATH, playlist.title)
if not os.path.isdir(path):
    os.mkdir(path)

for url in playlist:
    try:
        video = YouTube(url)
        print(f"Downloading...{video.title}")

        # check if title is already exists before downloading.
        video_path = os.path.join(path, f"{video.title}.mp4")
        if os.path.isfile(video_path):
            print("video already exists. skipping.....")
            continue

        stream = video.streams.get_highest_resolution()
        stream.download(output_path = path)
    except Exception as e:
        print(f"An error occured while downloading the video: {e}")