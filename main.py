'''
Created on Dec 3, 2018

@author: rabihkodeih
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, Gdk


class MainWindow(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self, title='CM')
        self.set_border_width(10)
        self.set_default_size(400, 600)
        #TODO: set fixes size, do not resize
        # header bar
        self.set_titlebar(self.create_header_bar())
        # main container
        main_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(main_container)
        # location selector
        location_selector = self.create_location_selector()
        main_container.pack_start(location_selector, True, True, 0)
        # todays date box
        todays_date_box = self.create_todays_date_box()
        main_container.pack_start(todays_date_box, True, True, 0)
        # weather point box
        weather_point_box = self.create_weather_point_box()
        main_container.pack_start(weather_point_box, True, True, 0)
        # weather day box
        weather_day_box = self.create_weather_day_box()
        main_container.pack_start(weather_day_box, True, True, 0)
        # weather week box
        weather_week_box = self.create_weather_week_box()
        main_container.pack_start(weather_week_box, True, True, 0)
        

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

    def create_todays_date_box(self):
        box = Gtk.Box()
        box.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(1.0, 0.8, 0.8, 1.0))
        label = Gtk.Label('todays_date_box') 
        box.pack_start(label, True, True, 0)
        return box

    def create_location_selector(self):
        box = Gtk.Box()
        box.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(0.8, 1.0, 0.8, 1.0))
        label = Gtk.Label('location_selector') 
        box.pack_start(label, True, True, 0)
        return box
    
    def create_weather_point_box(self):
        box = Gtk.Box()
        box.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(0.8, 0.8, 1.0, 1.0))
        label = Gtk.Label('weather_point_box') 
        box.pack_start(label, True, True, 0)
        return box
    
    def create_weather_day_box(self):
        box = Gtk.Box()
        box.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(1.0, 1.0, 0.8, 1.0))
        label = Gtk.Label('weather_day_box') 
        box.pack_start(label, True, True, 0)
        return box

    def create_weather_week_box(self):
        box = Gtk.Box()
        box.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(1.0, 0.8, 1.0, 1.0))
        label = Gtk.Label('weather_week_box') 
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

#TODO: https://stackoverflow.com/questions/19452797/draw-a-svg-image-in-gtk3-from-svg-source-in-python

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



#TODO: apply PEP8 formating








