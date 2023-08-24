# This script downloads the videos from a Youtube playlist by providing it with a URL to the playlist itself, and saves the files to a "videos" folder next to the script's file
from pytube import YouTube
from pytube import Playlist
import os

# I trust you have the rights to do this

# Insert the url of the playlist to download here
playlist = Playlist("https://www.youtube.com/playlist?list=OLAK5uy_kAwgb60W3p_xiZQ28HHJHVuDqsV0L7ZA4")

# Create a folder named "videos", if there's none in the folder the script is in
if not os.path.exists("videos"):
	os.makedirs("videos")

x = 0
for url in playlist:
	# We'll iterate through the entire playlist, and download each video like in the VideoDownload script.
	x = x+1
	# Shows on console the current video/total that's being processed, and its url
	print('('+str(x)+'/'+str(len(playlist.video_urls))+') - '+url)
	
	
	# If your video has 720p resolution or higher, you may want to set the res= attribute to "720p".
	# The script won't work if the video doesn't have the resolution you're asking from it (for example, it's an old video that only gets up to 240p)
	# Videos will be saved to the "videos" folder, as you'd expect. The filename is the title of the video
	# Keep in mind that music doesn't have a 480p resolution. You'll want to check 360p or 720p.
	YouTube(url).streams.filter(res="360p").first().download('videos/')
