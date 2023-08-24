# This script downloads a video from Youtube by providing it with a URL to the video, and saves the file to a "videos" folder next to the script's file
from pytube import YouTube
import os

# I trust you have the rights to do this

# Insert the url of the video to download here
url = "https://www.youtube.com/watch?v=Y5Wf0ytYHdA"

# Create a folder named "videos", if there's none in the folder the script is in
if not os.path.exists("videos"):
	os.makedirs("videos")

# If your video has 720p resolution or higher, you may want to set the res= attribute to "720p".
# The script won't work if the video doesn't have the resolution you're asking from it (for example, it's an old video that only gets up to 240p)
# Videos will be saved to the "videos" folder, as you'd expect. The filename is the title of the video
# Keep in mind that music doesn't have a 480p resolution. You'll want to check 360p or 720p.
YouTube(url).streams.filter(res="360p").first().download('videos/')
