import os
import moviepy.editor as mp

# Checks in a folder named "videos" that should be in the same folder the script is in
for filename in os.listdir('videos/'):
	
	# Gets name and extension, and prints the name to console
	name = filename.split('.')[0]
	print(name)
	ext = filename.split('.')[1]
	
	# Check if the extension is NOT .mp3, in which case we'll grab the file (you better only have video files here) and extract its audio, saving it to the same folder, with the same name as the video
	if ext != "mp3":
		clip = mp.VideoFileClip('videos/'+filename)
		clip.audio.write_audiofile('videos/'+name+'.mp3')