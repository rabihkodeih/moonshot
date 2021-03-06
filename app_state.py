import time
import storage
from datetime import datetime, timedelta
from utils import new_thread
from utils import fetch_weather_day_data
from utils import fetch_weather_week_data
from utils import fetch_weather_info_data
from storage import execute_query
from gi.repository import GLib
from settings import HISTORY_SAMPLING_PERIOD_HOURS


def async_update(main_window):
    async_update_weather_info_data(main_window)
    async_update_weather_day_data(main_window)
    async_update_weather_week_data(main_window)


@new_thread
def async_update_weather_info_data(main_window):
    location = get_current_location()
    if location:
        _, _, latitude, longitude = location
        data = fetch_weather_info_data(latitude, longitude)
        weather_info_data = {'weather_icon_code': data.get('weather', [{}])[0].get('icon', '02d'),
                             'temperature': data.get('main', {}).get('temp', '_'),
                             'wind_speed': data.get('wind', {}).get('speed', '_'),
                             'humidity': data.get('main', {}).get('humidity', '_')}
        storage.set_json_value('WEATHER_INFO_DATA', weather_info_data)
        # this ensures all Gtk operations happen on the main thread
        GLib.idle_add(main_window.refresh, 'weather_info')


@new_thread
def async_update_weather_day_data(main_window):
    location = get_current_location()
    if location:
        _, _, latitude, longitude = location
        weather_day_data = fetch_weather_day_data(latitude, longitude)
        storage.set_json_value('WEATHER_DAY_DATA', weather_day_data)
        # this ensures all Gtk operations happen on the main thread
        GLib.idle_add(main_window.refresh, 'weather_day')


@new_thread
def async_update_weather_week_data(main_window):
    location = get_current_location()
    if location:
        _, _, latitude, longitude = location
        weather_week_data = fetch_weather_week_data(latitude, longitude)
        storage.set_json_value('WEATHER_WEEK_DATA', weather_week_data)
        # this ensures all Gtk operations happen on the main thread
        GLib.idle_add(main_window.refresh, 'weather_week')


def get_next_sampling_time():
    now = datetime.now()
    sampling_time = now + timedelta(hours=HISTORY_SAMPLING_PERIOD_HOURS)
    sampling_time = sampling_time.replace(
        hour=(sampling_time.hour // HISTORY_SAMPLING_PERIOD_HOURS) * HISTORY_SAMPLING_PERIOD_HOURS,
        minute=0,
        second=0,
        microsecond=0
    )
    return sampling_time


@new_thread
def sample_historical_data():

    @new_thread
    def sample_weather_data(location):
        loc_id, _, latitude, longitude = location
        data = fetch_weather_info_data(latitude, longitude)
        temp = data.get('main', {}).get('temp')
        wind_speed = data.get('wind', {}).get('speed')
        humidity = data.get('main', {}).get('humidity')
        values = (loc_id, temp, wind_speed, humidity, datetime.now())
        query = ('INSERT INTO history (location_id, temperature, wind_speed, humidity, sample_time) '
                 'VALUES (?, ?, ?, ?, ?);')
        execute_query(query, values)

    # run sampling loop
    while True:
        sampling_time = get_next_sampling_time()
        while datetime.now() < sampling_time:
            time.sleep(10)
        for location in get_locations():
            sample_weather_data(location)


def get_historical_temp_data(location_id):
    query = 'SELECT temperature, sample_time FROM history WHERE location_id = %s ORDER BY sample_time DESC;'
    return execute_query(query % location_id)


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


def get_current_location():
    current_location_id = storage.get_text_value('CURRENT_LOCATION_ID')
    if current_location_id:
        query = 'SELECT id, name, latitude, longitude FROM locations WHERE id=%s' % current_location_id
        result = execute_query(query)
    else:
        result = None
    location = result[0] if result else None
    return location


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
        weather_day_data = [('____', '02d', '_'),
                            ('____', '02d', '_'),
                            ('____', '02d', '_'),
                            ('____', '02d', '_'),
                            ('____', '02d', '_'),
                            ('____', '02d', '_'),
                            ('____', '02d', '_'),
                            ('____', '02d', '_')]
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
