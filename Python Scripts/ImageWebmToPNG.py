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
	
	# Checks if the extension is .webp and if so, creates a copy of the image with .png extension
	# You can get rid of the check to make it convert all pictures; I would recommend making it check for pictures that are not .png in that case
	# If you want a different format, just specify it here. Python will do all the conversion work
	if ext == "webp":
		pic = Image.open(filename)
		pic.save("result/"+name+".png")
	