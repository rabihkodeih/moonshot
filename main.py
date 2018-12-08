'''
Created on Dec 3, 2018

@author: rabihkodeih
'''

import gi
from datetime import datetime
from utils import debug_background
from utils import create_image_form_svg
from utils import create_weather_data_widget
from utils import create_weather_period_widget
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
        weather_point_widget = self.create_weather_info_widget()
        main_container.pack_start(weather_point_widget, True, True, 10)
        weather_day_widget = self.create_weather_day_widget()
        main_container.pack_start(weather_day_widget, False, True, 50)
        weather_week_box = self.create_weather_week_widget()
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
    
    @debug_background(False)
    def create_weather_info_widget(self):
        box = Gtk.VBox()
        # weather info
        grid = Gtk.Grid()
        weather_image = create_image_form_svg(
            "assets/weather_icons/02d.svg",
            size = 128 + 32,
            margins=(25, 20, 0, 0)
        )
        weather_data_widget = create_weather_data_widget('23 \u00B0C', '11 kph', '95 %')
        grid.attach(weather_image, 1, 1, 1, 3)
        grid.attach(weather_data_widget, 3, 3, 1, 1)
        grid.props.valign = Gtk.Align.CENTER
        grid.props.halign = Gtk.Align.CENTER
        box.pack_start(grid, False, True, 0)
        # todays date
        label = Gtk.Label()
        today_1, today_2 = datetime.now().strftime('%A'), datetime.now().strftime('%B %d %Y')
        markup = ('<span font_size="xx-large" font_weight="bold">%s</span>\n' % today_1 +
                  '<span font_size="xx-large" font_weight="light">%s</span>' % today_2)
        label.set_markup(markup)
        label.set_justify(Gtk.Justification.LEFT) 
        box.pack_start(label, False, True, 0)
        return box
    
    @debug_background(False)
    def create_weather_day_widget(self):
        box = Gtk.Box()
        week_data = [('3 AM', '02d', 24),
                     ('6 AM', '09d', 24),
                     ('9 AM', '13d', 22),
                     ('NOON', '04d', 21),
                     ('3 PM', '50d', 34),
                     ('6 PM', '02d', 33),
                     ('9 PM', '02d', 33),
                     ('MIDN', '01d', 31)]
        for data in week_data:
            unit = create_weather_period_widget(*data)
            box.pack_start(unit, True, True, 0)
        return box

    @debug_background(False)
    def create_weather_week_widget(self):
        box = Gtk.Box()
        week_data = [('MON', '01d', 31, 23),
                     ('TUE', '02d', 33, 24),
                     ('WED', '09d', 32, 24),
                     ('THU', '13d', 32, 22),
                     ('FRI', '04d', 33, 21),
                     ('SAT', '50d', 34, 25),
                     ('SUN', '02d', 33, 24),]
        for data in week_data:
            unit = create_weather_period_widget(*data)
            box.pack_start(unit, True, True, 0)
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








