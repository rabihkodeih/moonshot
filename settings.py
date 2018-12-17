import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

WEATHER_ICONS_PATH = os.path.join(BASE_DIR, 'assets', 'weather_icons')

OPENWEATHERMAPAPI_KEY = "8eeed4e8cb01305d3b85e69f94685b38"

OPENWEATHERMAP_URL = "http://api.openweathermap.org/data/2.5"

HISTORY_SAMPLING_PERIOD_HOURS = 3

DB_CONFIG = {
    'DB_NAME': 'moonshot'
}


# end of file
