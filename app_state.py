'''
Created on Dec 8, 2018

@author: rabihkodeih
'''

import random
import time
import storage
from utils import new_thread


@new_thread
def async_update(main_window):
    print()
    print('=' * 70)
    print('async update')
    print('=' * 70)
    print()
    # TODO: implement actual API call
    time.sleep(0.25)  # simulates async call, where local state storage is actually updated
    weather_info_data = {'weather_icon_code': '02d',
                         'temperature': 23,
                         'wind_speed': random.randrange(5, 20),
                         'humidity': 76}
    storage.set_json_value('WEATHER_INFO_DATA', weather_info_data)
    weather_day_data = [('3 AM', '02d', random.randrange(21, 33)),
                        ('6 AM', '09d', random.randrange(21, 33)),
                        ('9 AM', '13d', random.randrange(21, 33)),
                        ('NOON', '04d', random.randrange(21, 33)),
                        ('3 PM', '50d', random.randrange(21, 33)),
                        ('6 PM', '02d', random.randrange(21, 33)),
                        ('9 PM', '02d', random.randrange(21, 33)),
                        ('MIDN', '01d', random.randrange(21, 33))]
    storage.set_json_value('WEATHER_DAY_DATA', weather_day_data)
    weather_week_data = [('MON', '01d', random.randrange(27, 33), random.randrange(21, 27)),
                         ('TUE', '02d', random.randrange(27, 33), random.randrange(21, 27)),
                         ('WED', '09d', random.randrange(27, 33), random.randrange(21, 27)),
                         ('THU', '13d', random.randrange(27, 33), random.randrange(21, 27)),
                         ('FRI', '04d', random.randrange(27, 33), random.randrange(21, 27)),
                         ('SAT', '50d', random.randrange(27, 33), random.randrange(21, 27)),
                         ('SUN', '02d', random.randrange(27, 33), random.randrange(21, 27))]
    storage.set_json_value('WEATHER_WEEK_DATA', weather_week_data)
    main_window.emit('refresh')


def get_locations():
    query = 'SELECT id, name, latitude, longitude FROM locations;'
    locations = ([str(f) for f in r] for r in storage.execute_query(query))
    return locations


def save_locations(locations, deleted_locations):
    persisted = {loc[0]: loc for loc in get_locations()}
    updated = []
    inserted = []
    if deleted_locations:
        deleted_ids = ', '.join(l[0] for l in deleted_locations)
        query = 'DELETE FROM locations WHERE id in (%s)' % deleted_ids
        storage.execute_query(query)
    for loc in locations:
        loc = list(loc)
        loc_id = loc[0]
        if loc_id == '-1':
            inserted.append(loc)
        elif loc != persisted[loc_id]:
            updated.append(loc)
    if inserted:
        values = ', '.join('(%s)' % ', '.join('"%s"' % f for f in loc[1:]) for loc in inserted)
        query = 'INSERT INTO locations (name, latitude, longitude) VALUES %s' % values
        storage.execute_query(query)
    if updated:
        for loc in updated:
            loc_id, name, latitude, longitude = loc
            query = 'UPDATE locations SET name="%s", latitude="%s", longitude="%s" WHERE ID=%s'
            query = query % (name, latitude, longitude, loc_id)
            storage.execute_query(query)            


def get_current_location_id():
    return storage.get_text_value('CURRENT_LOCATION_ID')


def set_current_location_id(location_id):
    storage.set_text_value('CURRENT_LOCATION_ID', str(location_id))


def get_weather_info_data():
    weather_info_data = storage.get_json_value("WEATHER_INFO_DATA")
    if weather_info_data is None:
        weather_info_data = {'weather_icon_code': '02d',
                             'temperature': '_',
                             'wind_speed': '_',
                             'humidity': '_'}
    return weather_info_data


def get_weather_day_data():
    weather_day_data = storage.get_json_value('WEATHER_DAY_DATA')
    if weather_day_data is None:
        weather_day_data = [('3 AM', '02d', '_'),
                            ('6 AM', '02d', '_'),
                            ('9 AM', '02d', '_'),
                            ('NOON', '02d', '_'),
                            ('3 PM', '02d', '_'),
                            ('6 PM', '02d', '_'),
                            ('9 PM', '02d', '_'),
                            ('MIDN', '02d', '_')]
    return weather_day_data


def get_weather_week_data():
    weather_week_data = storage.get_json_value('WEATHER_WEEK_DATA')
    if weather_week_data is None:
        weather_week_data = [('___', '02d', '_', '_'),
                             ('___', '02d', '_', '_'),
                             ('___', '02d', '_', '_'),
                             ('___', '02d', '_', '_'),
                             ('___', '02d', '_', '_'),
                             ('___', '02d', '_', '_'),
                             ('___', '02d', '_', '_')]
    return weather_week_data


# end of file
