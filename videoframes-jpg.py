import cv2 as cv
import numpy as np
import os
import datetime as dt
import shutil
# vidFile = str(input('Enter File name: ')) + '.mp4'
# ask: file format???
vidFile = 'example.mp4'

today = str(dt.date.today()).replace('-', '')
video = cv.VideoCapture(vidFile)
# ask: are we going to use live video feed?

try:
    dir_name = 'frames_' + today
    if os.path.exists(dir_name):
        print('Directory already exist')
        print('Deleting existing directory...')
        shutil.rmtree(dir_name)

    print('Creating directory ', dir_name + '...')
    os.makedirs(dir_name)

    #ask: do we take footages more than once a day?
except Exception as e1:
    print('Error creating directory...')
    print('Description: ', e)

currentFrame = 0
not_end = True
try:
    while(not_end):
        not_end, frame = video.read()
        file_name = 'frame-' + today + '-' + str(currentFrame)
        file_loc = './' + dir_name + '/' + file_name + '.jpg'
        print ('Saving frame:', currentFrame)
        cv.imwrite(file_loc, frame)
        currentFrame += 1

except Exception as e:
    print('Error writing image: ', e)

video.release()
pause
print('Frames are saved to ', dir_name)
# pause (5)
cv.destroyAllWindows()
