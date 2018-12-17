'''
Created on Dec 17, 2018

@author: rabihkodeih
'''

import gi
try:
    gi.require_version('Gtk', '3.0')
except Exception:
    raise

import random

from datetime import timedelta
from app_state import get_locations, get_next_sampling_time
from storage import execute_query
from settings import HISTORY_SAMPLING_PERIOD_HOURS


def sampling_time_sequence():
    current = get_next_sampling_time()
    for i in range(10):
        yield current - timedelta(hours=HISTORY_SAMPLING_PERIOD_HOURS*(i + 1))


if __name__ == '__main__':
    print("Inserting test historical weather data\n")

    data = [(6.0, 5.21, 61),
            (4.1, 4.06, 62),
            (3.0, 3.02, 62),
            (7.1, 2.41, 61),
            (7.5, 2.91, 63),
            (7.7, 4.40, 64),
            (8.2, 4.96, 65),
            (8.9, 5.32, 67),
            (9.6, 6.06, 67),
            (9.7, 6.74, 70)]

    execute_query('DELETE FROM history;')
    for loc_id, name, _, _ in get_locations():
        print('Generating historical data for %s' % name)
        temp_offset = 20*random.random()
        wind_speed_offset = 10*random.random()
        humidity_offset = 10*random.random()
        for d, sample_time in zip(data, sampling_time_sequence()):
            temp = '%.2f' % (d[0] + temp_offset)
            wind_speed = '%.2f' % (d[1] + wind_speed_offset)
            humidity = '%.2f' % (d[2] + humidity_offset)
            values = (loc_id, temp, wind_speed, humidity, sample_time)
            query = ('INSERT INTO history (location_id, temperature, wind_speed, humidity, sample_time) '
                     'VALUES (?, ?, ?, ?, ?);')
#             print(values)
            execute_query(query, values)

    print("\nDone")


# end of file
