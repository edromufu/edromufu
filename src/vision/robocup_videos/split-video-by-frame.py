'''
Using OpenCV takes a mp4 video and produces a number of images.
Requirements
----
You require OpenCV 3.2 to be installed.
Run
----
Open the main.py and edit the path to the video. Then run:
$ python main.py
Which will produce a folder called data with the images. There will be 2000+ images for example.mp4.
'''
import cv2
import numpy as np
import os

# Playing video from file:
nome_do_video = "film7"
cap = cv2.VideoCapture(nome_do_video + '.avi')

try:
    if not os.path.exists(nome_do_video):
        os.makedirs(nome_do_video)
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    name = './' + nome_do_video + '/frame' + str(currentFrame) + '.jpg'

    if currentFrame % 10 == 0:
        print ('Creating...' + name)
        cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()