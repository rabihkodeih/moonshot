'''
Created on Dec 8, 2018

@author: rabihkodeih
'''


import gi
from datetime import datetime
from utils import create_image_form_svg
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class WeatherInfoWidget(object):
    
    @staticmethod
    def info_widget(*info_list, font_size='x-large', font_weight='light', margins=None):
        container = Gtk.VBox()
        for info in info_list:
            box = Gtk.Box()
            label = Gtk.Label()
            markup = '<span font_size="%s" font_weight="%s">%s</span>' % (font_size, font_weight, info)
            label.set_markup(markup)
            if margins:
                top, right, bottom, left = margins
                label.set_margin_top(top)
                label.set_margin_left(left)
                label.set_margin_bottom(bottom)
                label.set_margin_right(right)
            box.add(label)
            container.pack_start(box, False, True, 0)
        return container
    
    def __init__(self):
        box = Gtk.VBox()
        # weather info
        grid = Gtk.Grid()
        weather_image = create_image_form_svg(
            "assets/weather_icons/02d.svg",
            size = 128 + 32,
            margins=(25, 20, 0, 0)
        )
        weather_data_widget = WeatherInfoWidget.info_widget('23 \u00B0C', '11 kph', '95 %')
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
        self.box = box

    def component(self):
        return self.box
    
    def refresh(self):
        pass
    
    
# end of file
