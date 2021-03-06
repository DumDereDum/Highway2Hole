import os
import sys
import cv2 as cv

from DBMS.DBMS import *
from functions.time_location import *
from map_painting.map.Map import *

# Preparation
script_location = os.path.split(os.path.realpath(sys.argv[0]))[0]
print(script_location)

terminal_command = script_location + "\\model\\Build\\Release\\OV_proj.exe" \
    + " --m=\"" + script_location + "\\model\\data\"" \
    + " --v=\"" + script_location + "\\model\\data\\short.mp4\"" \
    + " --o=\"" + script_location + "\\logs\""


# Pipline

## Model
print("\n<=== Model Run===>")
os.system(terminal_command)

## Matching
print("\n<=== Matching ===>")
start_date = get_start_date()
arr = get_times(start_date, script_location + "\logs\\log.txt")

## DBMS
print("\n<=== DBMS ===>")
db = DBMS_(script_location+'\\DBMS')

vidcap = cv2.VideoCapture(script_location + "\\logs\\out.avi")
# compute first 1000 frames
holes_counter = 0
for i in range(1000):
    success,image = vidcap.read()
    if holes_counter < 600 and arr[holes_counter][0] == i:
        date = convert_date(arr[holes_counter][1])
        coords = find_gps(arr[holes_counter][1], script_location + "\\logs\\gps_test_data.json")
        if coords != None:
            db.add_pothole(image, date, coords['latitude'], coords['longitude'])
        holes_counter += 10


## Map Painting
print("\n<=== Map Painting ===>")
potholes = db.get_new_potholes()
# potholes ~ [img, ID, PHOTO_PATH, TIME, GPS_LAT, GPS_LON, IS_NEW]
map = Map(script_location + "\\map_painting\\map")
map.update_map(potholes)


