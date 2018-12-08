'''
Created on Dec 8, 2018

@author: rabihkodeih
'''


import os
import gi
from datetime import datetime
from utils import svg_image_widget
from settings import WEATHER_ICONS_PATH
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class WeatherInfoWidget(object):
        
    def __init__(self):
        self.widget_weather_icon = None
        self.widget_temperature = None
        self.widget_wind_speed = None
        self.widget_humidity = None
        self.widget_todays_date = None

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
        widget.update = lambda text: label.set_markup(markup % (font_size, font_weight, text))
        return widget

    def component(self):        
        comp = Gtk.VBox()
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
        comp.pack_start(grid, False, True, 0)
        # todays date
        self.widget_todays_date = Gtk.Label()
        def update_todays_date(today):
            today_1, today_2 = today.split(',')
            markup = ('<span font_size="xx-large" font_weight="bold">%s</span>\n' % today_1 +
                      '<span font_size="xx-large" font_weight="light">%s</span>' % today_2)
            self.widget_todays_date.set_markup(markup)
        self.widget_todays_date.update = update_todays_date
        self.widget_todays_date.set_justify(Gtk.Justification.LEFT) 
        comp.pack_start(self.widget_todays_date, False, True, 0)
        comp.update = self.update
        return comp
    
    def update(self):
        #TODO: get relevant state from app_state
        today = datetime.now().strftime('%A,%B %d %Y')
        self.widget_weather_icon.update(os.path.join(WEATHER_ICONS_PATH, '%s.svg' % '02d'))
        self.widget_temperature.update('23 \u00B0C')        
        self.widget_wind_speed.update('11 kph')
        self.widget_humidity.update('95 %')
        self.widget_todays_date.update(today)
        

# end of file
