'''
Created on Dec 8, 2018

@author: rabihkodeih
'''

from datetime import datetime
import random


def get_locations():
    data = [('Paris', '0'),
            ('London', '1'),
            ('New York', '2'),
            ('Beirut', '3'),
            ('Helsinki', '4')]
    return data


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
