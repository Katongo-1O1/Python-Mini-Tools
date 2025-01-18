import os
import yt_dlp

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# URL of the YouTube video
url = 'https://www.youtube.com/watch?v=q5m09rqOoxE'

try:
    # Define download options
    ydl_opts = {
        'format': 'bestaudio[ext=webm]/bestaudio/best',  # Download best available audio
        'outtmpl': os.path.join(script_dir, '%(title)s.%(ext)s'),  # Save in script's location
    }

    # Use yt-dlp to download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(url, download=True)

    # Get the downloaded file path
    original_file = os.path.join(script_dir, f"{result['title']}.{result['ext']}")
    mp3_file = os.path.join(script_dir, f"{result['title']}.mp3")


except yt_dlp.utils.DownloadError as e:
    print(f"An error occurred during download: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
