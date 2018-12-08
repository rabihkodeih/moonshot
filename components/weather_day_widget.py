'''
Created on Dec 8, 2018

@author: rabihkodeih
'''


import os
import gi
from utils import svg_image_widget
from settings import WEATHER_ICONS_PATH
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class WeatherDayWidget(object):

    def period_widget(self):
        # period
        period = Gtk.VBox()
        # period label
        period_label = Gtk.Label()
        f_size = "12480"
        # weather image
        weather_image = svg_image_widget( size=32, margins=(5, 0, 5, 0))
        # temp box
        temp_box = Gtk.Box()
        temp_label = Gtk.Label()
        temp_box.pack_start(temp_label, True, True, 0)
        # update closure
        def update(period, icon_code, temp):
            markup = '<span font_size="%s" font_weight="light">%s</span>' % (f_size, period)
            period_label.set_markup(markup)
            weather_image.update(os.path.join(WEATHER_ICONS_PATH, '%s.svg' % icon_code))
            markup = '<span font_family="arial narrow" font_size="large" font_weight="light">%s\u00B0</span>' % temp
            temp_label.set_markup(markup)
        # render period
        period.pack_start(period_label, False, True, 0)
        period.pack_start(weather_image, False, True, 0)
        period.pack_start(temp_box, False, True, 0)
        period.update = update
        return period

    def __init__(self):
        self.widgets_periods = []
        
    def component(self):
        comp = Gtk.Box()
        for _ in range(8):
            period_widget = self.period_widget()
            self.widgets_periods.append(period_widget)
            comp.pack_start(period_widget, True, True, 0)
        comp.update = self.update
        return comp
    
    def update(self):
        #TODO: get relevant state from app_state
        day_data = [('3 AM', '02d', 24),
                     ('6 AM', '09d', 24),
                     ('9 AM', '13d', 22),
                     ('NOON', '04d', 21),
                     ('3 PM', '50d', 34),
                     ('6 PM', '02d', 33),
                     ('9 PM', '02d', 33),
                     ('MIDN', '01d', 31)]
        for data, widget in zip(day_data, self.widgets_periods):
            widget.update(*data)
    

# end of file
