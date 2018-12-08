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


class WeatherWeekWidget(object):

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
        # update closure
        def update(period, icon_code, temp_1, temp_2):
            markup = '<span font_size="%s" font_weight="light">%s</span>' % (f_size, period)
            period_label.set_markup(markup)
            weather_image.update(os.path.join(WEATHER_ICONS_PATH, '%s.svg' % icon_code))
            markup = '<span font_family="arial narrow" font_size="large" font_weight="light">%s\u00B0</span>' % temp_1
            temp_1_label.set_markup(markup)
            markup = '<span font_family="arial narrow" font_size="large" font_weight="light">%s\u00B0</span>' % temp_2
            temp_2_label.set_markup(markup)
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
        for _ in range(7):
            period_widget = self.period_widget()
            self.widgets_periods.append(period_widget)
            comp.pack_start(period_widget, True, True, 0)
        comp.update = self.update
        return comp
    
    def update(self):
        #TODO: get relevant state from app_state
        week_data = [('MON', '01d', 31, 23),
                     ('TUE', '02d', 33, 24),
                     ('WED', '09d', 32, 24),
                     ('THU', '13d', 32, 22),
                     ('FRI', '04d', 33, 21),
                     ('SAT', '50d', 34, 25),
                     ('SUN', '02d', 33, 24),]
        for data, widget in zip(week_data, self.widgets_periods):
            widget.update(*data)
    

# end of file
