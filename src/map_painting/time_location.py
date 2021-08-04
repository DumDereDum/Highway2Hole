import json


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
        date['seconds'] = seconds % 60
        date['minutes'] = seconds // 60 % 60
        date['hour'] = seconds // 3600 % 24
        date['day'] = seconds // 86400 % 30
        date['month'] = seconds // 2592000 % 12
        date['year'] = seconds // 31104000
        frame_times.append(date)
    for time in frame_times:
        for key in time.keys():
            time[key] += start_date[key]

    return [[frame_numbers[i], frame_times[i]] for i in range(len(frame_numbers))]


def find_gps(date, file_name):
    with open(file_name, 'r') as gps_json:
        json_dict = json.load(gps_json)
    for data in json_dict:
        if (data['time']['day'] == date['day']) and (data['time']['month'] == date['month']) and (data['time']['year'] == date['year']) and (data['time']['hour'] == date['hour']) and ((abs(data['time']['minutes'] - date['minutes']) <= 1) or ((abs(data['time']['seconds'] - date['seconds']) <= 40) and (data['time']['minutes'] == date['minutes']))):
            return data['location']
