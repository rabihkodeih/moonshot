'''
Created on Dec 8, 2018

@author: rabihkodeih
'''


import gi
from utils import create_image_form_svg
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class WeatherDayWidget(object):

    @staticmethod
    def period_widget(period, icon_code, temp_1, temp_2=None):
        # day label
        period_label = Gtk.Label()
        f_size = "12480" if temp_2 is None else "large"
        markup = '<span font_stretch="ultracondensed" font_size="%s" font_weight="light">%s</span>' % (f_size, period)
        period_label.set_markup(markup)
        # weather image
        i_size = 32 if temp_2 is None else 40
        weather_image = create_image_form_svg(
            "assets/weather_icons/%s.svg" % icon_code,
            size=i_size,
            margins=(5, 0, 5, 0)
        )
        # temp box
        temp_box = Gtk.Box()
        temp_1_label = Gtk.Label()
        markup = '<span font_family="arial narrow" font_size="large" font_weight="light">%s\u00B0</span>' % temp_1
        temp_1_label.set_markup(markup)
        temp_box.pack_start(temp_1_label, True, True, 0)
        if temp_2 is not None:
            temp_1_label.set_margin_left(6)
            temp_2_label = Gtk.Label()
            markup = '<span font_family="arial narrow" font_size="large" font_weight="light">%s\u00B0</span>' % temp_2
            temp_2_label.set_markup(markup)
            temp_2_label.set_margin_right(5)
            temp_box.pack_end(temp_2_label, True, True, 0)
        # container
        container = Gtk.VBox()
        container.pack_start(period_label, False, True, 0)
        container.pack_start(weather_image, False, True, 0)
        container.pack_start(temp_box, False, True, 0)
        return container

    def __init__(self):
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
            period_widget = WeatherDayWidget.period_widget(*data)
            box.pack_start(period_widget, True, True, 0)
        self.box = box
        
    def component(self):
        return self.box
    
    def refresh(self):
        pass
    

# end of file

