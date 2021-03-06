import random
import threading
import requests
import timezonefinder
import pytz

from datetime import datetime
from settings import OPENWEATHERMAPAPI_KEY
from settings import OPENWEATHERMAP_URL

from functools import wraps
from itertools import groupby
from gi.repository import Gtk, Gdk, GdkPixbuf


def correct_timezone(dt_value, latitude, longitude):
    '''
    Applies timezone correction to a date-time object
    using latitude and longitude information
    '''
    latitude, longitude = float(latitude), float(longitude)
    tf = timezonefinder.TimezoneFinder()
    timezone_str = tf.certain_timezone_at(lat=latitude, lng=longitude)
    if timezone_str is None:
        tz_corrected = dt_value
    else:
        timezone = pytz.timezone(timezone_str)
        tz_corrected = dt_value + timezone.utcoffset(dt_value)
    return tz_corrected


def fetch_weather_info_data(latitude, longitude):
    '''
    This function gets the weather info data from the online
    weather ervice using the following api endpoint defined in
    constants.py. The inputs are lat-long based coordinates.
    '''
    location_query = 'lat=%s&lon=%s' % (latitude, longitude)
    units_query = 'units=metric'
    auth_query = 'APPID=%s' % OPENWEATHERMAPAPI_KEY
    url = "%s/weather?%s&%s&%s" % (OPENWEATHERMAP_URL, location_query, units_query, auth_query)
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
    else:
        data = {}
    return data


def fetch_weather_day_data(latitude, longitude):
    '''
    This function gets the weather day forecast data from the online
    weather ervice using the following api endpoint defined in
    constants.py. The inputs are lat-long based coordinates.
    '''
    location_query = 'lat=%s&lon=%s' % (latitude, longitude)
    units_query = 'units=metric'
    auth_query = 'APPID=%s' % OPENWEATHERMAPAPI_KEY
    url = "%s/forecast?%s&%s&%s" % (OPENWEATHERMAP_URL, location_query, units_query, auth_query)
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
    else:
        data = {}
    forecasts = data.get('list', [])
    forecasts += [{}]*8
    weather_day_data = []
    for f in forecasts[:8]:
        forecast_time = f.get('dt_txt')
        if forecast_time:
            tmp = datetime.strptime(forecast_time, '%Y-%m-%d %H:%M:%S')
            tmp = correct_timezone(tmp, latitude, longitude)
            forecast_time = datetime.strftime(tmp, '%-I %p')
            forecast_time = forecast_time.replace('12 PM', 'NOON').replace('12 AM', 'MIDN')
        else:
            forecast_time = '____'
        icon_code = f.get('weather', [{}])[0].get('icon', '02d')
        temperature = f.get('main', {}).get('temp', '_')
        weather_day_data.append((forecast_time, icon_code, temperature))
    return weather_day_data


def fetch_weather_week_data(latitude, longitude):
    '''
    This function gets the weather week forecast data from the online
    weather ervice using the following api endpoint defined in
    constants.py. The inputs are lat-long based coordinates.
    '''
    location_query = 'lat=%s&lon=%s' % (latitude, longitude)
    units_query = 'units=metric'
    auth_query = 'APPID=%s' % OPENWEATHERMAPAPI_KEY
    url = "%s/forecast?%s&%s&%s" % (OPENWEATHERMAP_URL, location_query, units_query, auth_query)
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
    else:
        data = {}
    forecasts = data.get('list', [])
    weather_week_data = []
    for f in forecasts:
        forecast_time = f.get('dt_txt')
        if forecast_time:
            tmp = datetime.strptime(forecast_time, '%Y-%m-%d %H:%M:%S')
            week_day = datetime.strftime(tmp, '%a').upper()
        else:
            week_day = '___'
        icon_code = f.get('weather', [{}])[0].get('icon', '02d')
        if icon_code.endswith('n'):
            icon_code = icon_code[:-1] + 'd'
        temp = f.get('main', {}).get('temp', '_')
        weather_week_data.append((week_day, icon_code, temp))
    groups = [list(j) for _, j in groupby(weather_week_data, key=lambda x:x[0])]
    weather_week_data = []
    for g in groups:
        week_day = g[0][0]
        temp_min = int(round(min(g, key=lambda x: x[2])[2]))
        temp_max = int(round(max(g, key=lambda x: x[2])[2]))
        icon_code = g[len(g)//2][1]
        weather_week_data.append((week_day, icon_code, temp_min, temp_max))
    return weather_week_data


def debug_background(show):
    '''
    This decorator adds a background color to any widget returned
    by a function, very useful for debugging layouts and positioning.
    '''
    rgba = [0.5 + 0.5*random.random() for _ in range(3)]
    rgba.append(1.0)

    def real_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            widget = func(*args, **kwargs)
            if show:
                widget.override_background_color(
                    Gtk.StateType.NORMAL,
                    Gdk.RGBA(*rgba)
                )
            return widget
        return wrapper
    return real_decorator


def svg_image_widget(size=128, margins=None):
    '''
    This function returns a PyGobject image object given an svg
    input path. The returned object has an unpdate method having the
    following the signature refresh(svg_path) which should be called
    in order to actually render the svg path.
    '''
    width = -1
    height = size
    preserve_aspect_ratio = True
    image = Gtk.Image()

    def refresh_svg(svg_path):
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            svg_path, width, height, preserve_aspect_ratio)
        image.set_from_pixbuf(pixbuf)
    image.refresh = refresh_svg
    if margins:
        top, right, bottom, left = margins
        image.set_margin_top(top)
        image.set_margin_left(left)
        image.set_margin_bottom(bottom)
        image.set_margin_right(right)
    return image


def new_thread(func):
    '''
    This decorator runs <func> in a separate thread so as not to block
    the main Gtk UI thread.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.daemon = True
        thread.start()
        return thread
    return wrapper


# end of file
