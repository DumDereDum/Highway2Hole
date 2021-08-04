import sys
import json

sys.path.append('../../DBMS')
from DBMS import *


class Map:
    def __init__(self, path):
        self.path_to_data = path + "\\data.json"

    def create_map(self):
        pass

    def update_map(self, potholes):
        # potholes ~ [img, ID, PHOTO_PATH, TIME, GPS_LAT, GPS_LON, IS_NEW]
        data_file = open(self.path_to_data, "r")
        data = json.load(data_file)

        for pothole in potholes:
            json_data = {
                'time': pothole[3],
                'location': {
                    'latitude': pothole[-2],
                    'longitude': pothole[-1]
                }
            }
            ##
            ## process pothole to json_data
            ##
            data.append(json_data)
        data_file.close()
        data_file = open(self.path_to_data, "w")
        data_file.close()
        data_file = open(self.path_to_data, "r+")
        json.dump(data, data_file)

    def render(self):
        pass

# map = Map()
# map.update_map([['img', 'id', 'time', '2.2345', '1.0334', 'isnew']])
