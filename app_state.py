'''
Created on Dec 8, 2018

@author: rabihkodeih
'''

import random
import time
import storage
from datetime import datetime
from utils import new_thread



@new_thread
def async_update(main_window):
    time.sleep(0.25)  # simulates async call, where local state storage is actually updated
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
    return '5'


def set_current_location_id(location_id):
    # TODO: implement with actual DB access
    pass


def get_weather_info_data():
    #TODO: get todays_date according to the timezone of the currently selected loation
    data = {'weather_icon_code': '02d',
            'temperature': 23,
            'wind_speed': random.randrange(5, 20),
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
