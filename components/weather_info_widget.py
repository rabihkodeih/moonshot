'''
Created on Dec 8, 2018

@author: rabihkodeih
'''


import os
import gi
from datetime import datetime
from utils import svg_image_widget
from settings import WEATHER_ICONS_PATH
from app_state import get_weather_info_data
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject


class WeatherInfoWidget(Gtk.VBox):
        
    def __init__(self):
        Gtk.VBox.__init__(self)
        self.widget_weather_icon = None
        self.widget_temperature = None
        self.widget_wind_speed = None
        self.widget_humidity = None
        self.widget_todays_date = None
        self.init_components()

    @GObject.Signal
    def refresh(self):
        data = get_weather_info_data()
        self.widget_weather_icon.refresh(os.path.join(WEATHER_ICONS_PATH, '%s.svg' % data['weather_icon_code']))
        self.widget_temperature.refresh('%s \u00B0C' % data['temperature'])        
        self.widget_wind_speed.refresh('%s mps' % data['wind_speed'])
        self.widget_humidity.refresh('%s %%' % data['humidity'])
        self.widget_todays_date.refresh(datetime.now().strftime('%A,%B %d %Y'))

    def text_widget(self, font_size='x-large', font_weight='light', margins=None):
        widget = Gtk.Box()
        label = Gtk.Label()
        if margins:
            top, right, bottom, left = margins
            label.set_margin_top(top)
            label.set_margin_left(left)
            label.set_margin_bottom(bottom)
            label.set_margin_right(right)
        widget.add(label)
        markup = '<span font_size="%s" font_weight="%s">%s</span>'
        widget.refresh = lambda text: label.set_markup(markup % (font_size, font_weight, text))
        return widget

    def init_components(self):        
        # weather info
        grid = Gtk.Grid()
        self.widget_weather_icon = svg_image_widget(
            size = 128 + 32,
            margins=(25, 20, 0, 0)
        )
        weather_data_widget = Gtk.VBox()
        self.widget_temperature = self.text_widget()
        self.widget_wind_speed = self.text_widget()
        self.widget_humidity = self.text_widget()
        weather_data_widget.pack_start(self.widget_temperature, False, True, 0)
        weather_data_widget.pack_start(self.widget_wind_speed, False, True, 0)
        weather_data_widget.pack_start(self.widget_humidity, False, True, 0)
        grid.attach(self.widget_weather_icon, 1, 1, 1, 3)
        grid.attach(weather_data_widget, 3, 3, 1, 1)
        grid.props.valign = Gtk.Align.CENTER
        grid.props.halign = Gtk.Align.CENTER
        self.pack_start(grid, False, True, 0)
        # todays date
        self.widget_todays_date = Gtk.Label()
        def refresh_todays_date(today):
            today_1, today_2 = today.split(',')
            markup = ('<span font_size="xx-large" font_weight="bold">%s</span>\n' % today_1 +
                      '<span font_size="xx-large" font_weight="light">%s</span>' % today_2)
            self.widget_todays_date.set_markup(markup)
        self.widget_todays_date.refresh = refresh_todays_date
        self.widget_todays_date.set_justify(Gtk.Justification.LEFT) 
        self.pack_start(self.widget_todays_date, False, True, 0)
            

# end of file
