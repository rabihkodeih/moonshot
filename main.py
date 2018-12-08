'''
Created on Dec 3, 2018

@author: rabihkodeih
'''

import gi
from utils import debug_background
from utils import create_weather_period_widget
from components.weather_info_widget import WeatherInfoWidget
from components.weather_day_widget import WeatherDayWidget
from components.weather_week_widget import WeatherWeekWidget
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio


class MainWindow(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self, title='CM')
        self.set_border_width(10)
        self.set_default_size(400, 600)
        self.props.resizable = False
        self.set_titlebar(self.create_header_bar())
        main_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(main_container)
        
        location_selector = self.create_location_selector()
        
        main_container.pack_start(location_selector, False, True, 10)
        weather_info_widget = WeatherInfoWidget().component()
        
        main_container.pack_start(weather_info_widget, True, True, 10)
        weather_day_widget = WeatherDayWidget().component()
        
        main_container.pack_start(weather_day_widget, False, True, 50)
        weather_week_box = WeatherWeekWidget().component()
        
        main_container.pack_start(weather_week_box, False, True, 10)
        

    def create_header_bar(self):
        hb = Gtk.HeaderBar()
        hb.set_decoration_layout("menu:close")
        hb.set_show_close_button(True)
        hb.props.title = "Moonshot"
        # refresh button
        icon = Gio.ThemedIcon(name="view-refresh-symbolic")
        refresh_btn = Gtk.Button(None, image=Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON))
        hb.pack_start(refresh_btn)
        # temperature chart button
        icon = Gio.ThemedIcon(name="utilities-system-monitor-symbolic")
        tmpchart_btn = Gtk.Button(None, image=Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON))
        hb.pack_start(tmpchart_btn)
        # settings button
        icon = Gio.ThemedIcon(name="emblem-system-symbolic")
        settings_btn = Gtk.Button(None, image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON))
        hb.pack_start(settings_btn)
        return hb

    @debug_background(True)
    def create_location_selector(self):
        #TODO: implement
        box = Gtk.Box()
        label = Gtk.Label('location_selector') 
        box.pack_start(label, True, True, 0)
        return box
        

      
def launch_main_window():
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()


if __name__ == '__main__':
    print('Starting...\n')
    
    launch_main_window()

    print('\nDone.')
    

# end of file



# SPECS:
# Locations (1+)
# Display weather for at least 24 hours ahead
# refresh/update for weather data
# keep historical records
# use history to provide temperature chart

# API:
# api.openweathermap.org/data/2.5/weather?q={city name}
# api.openweathermap.org/data/2.5/weather?q={city name},{country code}
# api.openweathermap.org/data/2.5/weather?id={city_id}
# api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}
# api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}
# JSON response (Only really measured or calculated data is displayed in API response):
# weather condition codes: https://openweathermap.org/weather-conditions



#TODO: https://stackoverflow.com/questions/19452797/draw-a-svg-image-in-gtk3-from-svg-source-in-python
#TODO: apply PEP8 formating
#TODO: add documentation where it counts








