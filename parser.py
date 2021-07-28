import gpxpy
import gpxpy.gpx
import json
import sys


def get_time(point):
    day = point.time.day
    month = point.time.month
    year = point.time.year
    hour = point.time.hour
    minutes = point.time.minute
    seconds = point.time.second
    return {
        'day': day,
        'month': month,
        'year': year,
        'hour': hour,
        'minutes': minutes,
        'seconds': seconds
    }


def get_coordinates(point):
    latitude = point.latitude
    longitude = point.longitude
    return {
        'latitude': latitude,
        'longitude': longitude
    }


def get_info(point):
    return {
        'time': get_time(point),
        'location': get_coordinates(point)
    }


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('input must contain gpx file!')
        exit()

    gpx_file = open(sys.argv[1], 'r')
    gpx = gpxpy.parse(gpx_file)

    time_coord_list = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                time_coord_list.append(get_info(point))

    for point in gpx.waypoints:
        time_coord_list.append(get_info(point))

    for route in gpx.routes:
        for point in route.points:
            time_coord_list.append(get_info(point))

    with open(sys.argv[1].split('.')[0] + '.json', 'w') as f:
        json.dump(time_coord_list, f)
