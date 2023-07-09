import tkinter as tk
from pytube import YouTube

def download_video():
    video_url = url_entry.get()
    quality = quality_var.get()
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution(quality)
        stream.download()
        status_label.config(text="Download successful!")
    except Exception as e:
        status_label.config(text=str(e))

# Create the main Tkinter window
window = tk.Tk()
window.title("YouTube Video Downloader")

# Create the URL label and entry field
url_label = tk.Label(window, text="Enter YouTube URL:")
url_label.pack()
url_entry = tk.Entry(window)
url_entry.pack()

# Create the quality label and drop-down menu
quality_label = tk.Label(window, text="Select video quality:")
quality_label.pack()
quality_var = tk.StringVar(window)
quality_dropdown = tk.OptionMenu(window, quality_var, "360p", "480p", "720p", "1080p")
quality_dropdown.pack()

# Create the download button
download_button = tk.Button(window, text="Download", command=download_video)
download_button.pack()

# Create the status label
status_label = tk.Label(window, text="")
status_label.pack()

# Start the main Tkinter event loop
window.mainloop()
