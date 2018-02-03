'''
The goal is to extract only the parts of the mouth crops from the full videos which includes the whole face and other backgrounds.



python extracting_mouth_crops.py [source directory] [filetyoe] [target directory] [face predictor path]

filetype: *.avi, *.mpg, etc



'''
from videos import Video
import os,fnmatch,sys,errno

from skimage import io

SOURCE_PATH = sys.argv[1]
SOURCE_EXTENSION = sys.argv[2]
TARGET_PATH = sys.argv[3]

FACE_PREDICTOR_PATH = sys.argv[4]

def make_directory(path):
	try:
		os.makedirs(path)
	except OSError as exc:
		if exc.errno == errno.EEXIST and os.path.isdir(path):
			pass
		else:
			raise


def find_files(directory, pattern):
	for root, dirs, files in os.walk(directory):
		for basename in files:
			if fnmatch.fnmatch(basename, pattern):
				filename = os.path.join(root, basename)
				yield filename

for filepath in find_files(SOURCE_PATH, SOURCE_EXTENSION):
	print "Processing: {}".format(filepath)
	video= Video(vtype='face', face_predictor_path = FACE_PREDICTOR_PATH).from_video(filepath)
	
	filepath_wo_extension = os.path.splitext(filepath)[0]
	target_dir = os.path.join(TARGET_PATH, filepath_wo_extension)
	make_directory(target_dir)


	

	i=0
	for frame in video.mouth:
		io.imsave(os.path.join(target_dir,"mouth_{0:03d}.png".format(i)),frame)
		i+=1
