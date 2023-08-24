# This script will look for non-gif files in the folder it is in, scale them down to a set maximum height/width, convert them to .png and store the finished image in a "result" folder
import os
import math
from PIL import Image

# The script will look for files in the folder it is in
readDir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# If necessary, make a "result" folder to put our converted images into
if not os.path.exists("result"):
	os.makedirs("result")

for filename in os.listdir(readDir):
	
	# Ignore files with no extension (such as folders)
	if (len(filename.split('.')) < 2):
		continue

	# Gets the name of the file and the extension
	name = filename.split('.')[0]
	print(name)
	ext = filename.split('.')[1]
	
	# Ignore .gif files as these tend to be animated
	# Also ignore .py to the script ignores its own file
	if ext == "gif":
		continue
	elif ext == "py":
		continue
	pic = Image.open(filename)
	
	scl = pic.size
	scaleFactor = 1
	scaleResult = 1
	
	# We do some math to resize the picture to a maximum of 800 pixels in either dimension.
	# The scaling is proportional for both sides, so a 1200x900 file will end up as 800x600
	if scl[0] > scl[1]:
		if scl[0] > 800:
			scaleFactor = scl[0]/800
			pic = pic.resize((math.floor(scl[0]/scaleFactor), math.floor(scl[1]/scaleFactor)))
	elif scl[1] > scl[0]:
		if scl[1] > 800:
			scaleFactor = scl[1]/800
			pic = pic.resize((math.floor(scl[0]/scaleFactor), math.floor(scl[1]/scaleFactor)))
			
	# Save the modified picture to the results folder, with .png format
	# If you want a different format, just specify it here. Python will do all the conversion work
	pic.save("result/"+name+".png")
	
