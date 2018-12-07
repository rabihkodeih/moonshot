'''
Created on Dec 8, 2018

@author: rabihkodeih
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


def text_box(text, font_size='x-large', font_weight='light', margins=None):
    box = Gtk.Box()
    label = Gtk.Label()
    markup = '<span size="%s" font_weight="%s">%s</span>' % (font_size, font_weight, text)
    label.set_markup(markup)
    if margins:
        top, left, bottom, right = margins
        label.set_margin_top(top)
        label.set_margin_left(left)
        label.set_margin_bottom(bottom)
        label.set_margin_right(right)
    box.pack_start(label, False, True, 0)
    return box

# end of file