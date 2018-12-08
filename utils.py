'''
Created on Dec 8, 2018

@author: rabihkodeih
'''

import gi
from functools import wraps
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf


def create_weather_data_widget(*info_list, font_size='x-large', font_weight='light', margins=None):
    container = Gtk.VBox()
    for info in info_list:
        box = Gtk.Box()
        label = Gtk.Label()
        markup = '<span size="%s" font_weight="%s">%s</span>' % (font_size, font_weight, info)
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


def debug_background(rgba, show):
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


# end of file