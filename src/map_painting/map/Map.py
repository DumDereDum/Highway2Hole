import sys
import json

sys.path.append('../../DBMS')
from DBMS import *


class Map:
    def __init__(self):
        self.path_to_data = './data.json'

    def create_map(self):
        pass

    def update_map(self, potholes):
        data_file = open(self.path_to_data, "r")
        data = json.load(data_file)

        for pothole in potholes:
            json_data = {
                'time': {
                    'day': -1,
                    'month': -1,
                    'year': -1,
                    'hour': -1,
                    'minutes': -1,
                    'seconds': -1
                },
                'location': {
                    'latitude': -1,
                    'longitude': -1
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
