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


def svg_image_widget(size=128, margins=None):
    width = -1
    height = size
    preserve_aspect_ratio = True
    image = Gtk.Image()
    def update_svg(svg_path):
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(svg_path, width, height, preserve_aspect_ratio)
        image.set_from_pixbuf(pixbuf)
    image.update = update_svg
    if margins:
        top, right, bottom, left = margins
        image.set_margin_top(top)
        image.set_margin_left(left)
        image.set_margin_bottom(bottom)
        image.set_margin_right(right)
    return image


# TODO: deprecate and remove
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


# end of file