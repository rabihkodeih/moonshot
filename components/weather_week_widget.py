'''
Created on Dec 8, 2018

@author: rabihkodeih
'''


import os
import gi
import threading
from utils import svg_image_widget
from settings import WEATHER_ICONS_PATH
from app_state import get_weather_week_data
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class WeatherWeekWidget(Gtk.Box):

    def __init__(self):
        Gtk.Box.__init__(self)        
        self.widgets_periods = []
        self.init_components()

    def refresh(self):
        print('weather_week_widget:', threading.get_ident())
        week_data = get_weather_week_data()
        for data, widget in zip(week_data, self.widgets_periods):
            widget.refresh(*data)

    def period_widget(self):
        # period
        period = Gtk.VBox()
        # period label
        period_label = Gtk.Label()
        f_size = "large"
        # weather image
        weather_image = svg_image_widget(size=40, margins=(5, 0, 5, 0))
        # temp box
        temp_box = Gtk.Box()
        temp_1_label = Gtk.Label()
        temp_1_label.set_margin_left(6)
        temp_box.pack_start(temp_1_label, True, True, 0)
        temp_2_label = Gtk.Label()
        temp_2_label.set_margin_right(5)
        temp_box.pack_end(temp_2_label, True, True, 0)
        # refresh closure
        def refresh(period, icon_code, temp_1, temp_2):
            markup = '<span font_size="%s" font_weight="light">%s</span>' % (f_size, period)
            period_label.set_markup(markup)
            weather_image.refresh(os.path.join(WEATHER_ICONS_PATH, '%s.svg' % icon_code))
            markup = '<span font_family="arial narrow" font_size="large" font_weight="light">%s\u00B0</span>' % temp_1
            temp_1_label.set_markup(markup)
            markup = '<span font_family="arial narrow" font_size="large" font_weight="light">%s\u00B0</span>' % temp_2
            temp_2_label.set_markup(markup)
        # render period
        period.pack_start(period_label, False, True, 0)
        period.pack_start(weather_image, False, True, 0)
        period.pack_start(temp_box, False, True, 0)
        period.refresh = refresh
        return period

    def init_components(self):
        for _ in range(7):
            period_widget = self.period_widget()
            self.widgets_periods.append(period_widget)
            self.pack_start(period_widget, True, True, 0)

    
# end of file
