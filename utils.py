'''
Created on Dec 8, 2018

@author: rabihkodeih
'''

import random
import gi
from functools import wraps
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf


def debug_background(show):
    rgba = [0.5 + 0.5*random.random() for _ in range(3)]
    rgba.append(1.0)
    def real_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            widget = func(*args, **kwargs)
            if show:
                widget.override_background_color(
                    Gtk.StateType.NORMAL,
                    Gdk.RGBA(*rgba)
                )
            return widget
        return wrapper
    return real_decorator


def create_weather_data_widget(*info_list, font_size='x-large', font_weight='light', margins=None):
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


def create_image_form_svg(svg_path, size=128, margins=None):
    width = -1
    height = size
    preserve_aspect_ratio = True
    pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(svg_path, width, height, preserve_aspect_ratio)
    image = Gtk.Image()
    image.set_from_pixbuf(pixbuf)
    if margins:
        top, right, bottom, left = margins
        image.set_margin_top(top)
        image.set_margin_left(left)
        image.set_margin_bottom(bottom)
        image.set_margin_right(right)
    return image


def create_weather_week_unit_widget(day, icon_code, day_temp, night_temp):
    # day label
    day_label = Gtk.Label()
    markup = '<span font_stretch="ultracondensed" font_size="large" font_weight="light">%s</span>' % day
    day_label.set_markup(markup)
    # weather image
    weather_image = create_image_form_svg(
        "assets/weather_icons/%s.svg" % icon_code,
        size=36,
        margins=(5, 0, 5, 0)
    )
    # temp box
    temp_box = Gtk.Box()
    day_temp_label = Gtk.Label()
    markup = '<span font_family="arial narrow" font_size="large" font_weight="light">%s\u00B0</span>' % day_temp
    day_temp_label.set_markup(markup)
    day_temp_label.set_margin_left(6)
    temp_box.pack_start(day_temp_label, True, True, 0)
    night_temp_label = Gtk.Label()
    markup = '<span font_family="arial narrow" font_size="large" font_weight="light">%s\u00B0</span>' % night_temp
    night_temp_label.set_markup(markup)
    night_temp_label.set_margin_right(5)
    temp_box.pack_end(night_temp_label, True, True, 0)
    # container
    container = Gtk.VBox()
    container.pack_start(day_label, False, True, 0)
    container.pack_start(weather_image, False, True, 0)
    container.pack_start(temp_box, False, True, 0)
    return container


# end of file