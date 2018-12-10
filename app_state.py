'''
Created on Dec 8, 2018

@author: rabihkodeih
'''

import random
import time
from datetime import datetime
from utils import new_thread



@new_thread
def async_update(main_window):
    time.sleep(0.25)  # simulates async call, where local state storage is actually updated
    main_window.emit('refresh')


def get_locations():
    data = [('10', 'Paris', 'coord_0'),
            ('11', 'London', 'coord_1'),
            ('12', 'New York', 'coord_2'),
            ('13', 'Beirut', 'coord_3'),
            ('14', 'Helsinki', 'coord_4')]
    return data


def get_current_location_id():
    return '14'


def set_current_location(location_id):
    # TODO: implement with actual DB access
    pass


def get_weather_info_data():
    #TODO: get todays_date according to the timezone of the currently selected loation
    data = {'weather_icon_code': '02d',
            'temperature': 23,
            'wind_speed': random.randrange(5, 20),# 11,
            'humidity': 76,
            'todays_date': datetime.now().strftime('%A,%B %d %Y')}
    return data


def get_weather_day_data():
    day_data = [('3 AM', '02d', 24),
                ('6 AM', '09d', 24),
                ('9 AM', '13d', 22),
                ('NOON', '04d', 21),
                ('3 PM', '50d', 34),
                ('6 PM', '02d', 33),
                ('9 PM', '02d', 33),
                ('MIDN', '01d', 31)]
    return day_data


def get_weather_week_data():
    week_data = [('MON', '01d', 31, 23),
                 ('TUE', '02d', 33, 24),
                 ('WED', '09d', 32, 24),
                 ('THU', '13d', 32, 22),
                 ('FRI', '04d', 33, 21),
                 ('SAT', '50d', 34, 25),
                 ('SUN', '02d', 33, 24)]
    return week_data


# end of file
