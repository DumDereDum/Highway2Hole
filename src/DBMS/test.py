import os
import sys
import cv2 as cv

from DBMS import *

SCRIPT_DIR = os.path.split(os.path.realpath(sys.argv[0]))[0]
img = cv.imread(SCRIPT_DIR + "\\data\\test\\test_img.jpg")
db = DBMS(SCRIPT_DIR)
db.add_pothole(img, '1', '2')
res = db.get_new_potholes()
cv.imshow("res", res[0][0])
cv.waitKey(1000)
print("res = " + str(res[0][1:]))