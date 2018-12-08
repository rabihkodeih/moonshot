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


def create_weather_period_widget(period, icon_code, temp_1, temp_2=None):
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


# end of file