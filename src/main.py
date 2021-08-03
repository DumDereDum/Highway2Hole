import os
import sys
import cv2 as cv

from DBMS.DBMS import *

# Preparation
script_location = os.path.split(os.path.realpath(sys.argv[0]))[0]
print(script_location)

terminal_command = script_location + "\model\Release\OV_proj.exe" \
    + " --m=\"" + script_location + "\model\data\"" \
    + " --v=\"" + script_location + "\model\data\short.mp4\"" \
    + " --o=\"" + script_location + "\logs\""


# Pipline

## Model
os.system(terminal_command)

## DBMS

img = cv.imread(script_location + "\\DBMS\\data\\test\\test_img.jpg")
#cv.imshow('test', img)

db = DBMS(script_location+'\DBMS')
db.add_pothole(img, '1', '2')
potholes = db.get_new_potholes()
# potholes ~ [img, ID, PHOTO_PATH, TIME, GPS_LAT, GPS_LON, IS_NEW]
print(potholes)
