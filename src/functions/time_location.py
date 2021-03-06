import json
import os


def get_start_date(video_name='FILE20210715-194316-004604.MP4'):
    date = video_name.split('-')[0][4:]
    time = video_name.split('-')[1]
    date_dict = {'day': int(date[6:]), 'month': int(date[4:6]), 'year': int(date[:4]), 'hour': int(time[:2]), 'minutes': int(time[2:4]), 'seconds': int(time[4:])}
    return date_dict


def get_times(start_date, log_name="log.txt", fps=30):
    frame_numbers = []
    with open(log_name, 'r') as log:
        for line in log:
            frame_numbers.append(int(line.split("=")[1]))

    frame_seconds = []
    for num in frame_numbers:
        frame_seconds.append(num / fps)

    frame_times = []
    for seconds in frame_seconds:
        date = {'day': 0, 'month': 0, 'year': 0, 'hour': 0, 'minutes': 0, 'seconds': 0}
        date['seconds'] = int(seconds % 60)
        date['minutes'] = int(seconds // 60 % 60)
        date['hour'] = int(seconds // 3600 % 24)
        date['day'] = int(seconds // 86400 % 30)
        date['month'] = int(seconds // 2592000 % 12)
        date['year'] = int(seconds // 31104000)
        frame_times.append(date)
    for time in frame_times:
        for key in time.keys():
            time[key] += start_date[key]

    return [[frame_numbers[i], frame_times[i]] for i in range(len(frame_numbers))]


def find_gps(date, file_name):
    with open(file_name, 'r') as gps_json:
        json_dict = json.load(gps_json)
    for data in json_dict:
        if (data['time']['day'] == date['day']) \
        and (data['time']['month'] == date['month']) \
        and (data['time']['year'] == date['year']) \
        and (data['time']['hour'] + 3 == date['hour']) \
        and (abs(data['time']['minutes'] == date['minutes'])) \
        and (abs(data['time']['seconds'] - (date['seconds'] + 15)) <= 2):
            return data['location']


def convert_date(date):
    str_date = [str(date['day']), str(date['month']), str(date['year'])]
    str_time = [str(date['hour']), str(date['minutes']), str(date['seconds'])]
    return '.'.join(str_date) + ' ' + ':'.join(str_time)

if __name__ == '__main__':
    start_date = get_start_date()
    arr = get_times(start_date)
    print(convert_date(arr[0][1]))
    print(find_gps(arr[0][1], 'Jul_15_2021_7_38_22_PM.json'))
