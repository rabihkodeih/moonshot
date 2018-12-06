'''
Created on Dec 3, 2018

@author: rabihkodeih
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio


class HeaderBarWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="HeaderBar Demo")
        self.set_border_width(10)
        self.set_default_size(400, 200)

        #=======================================================================
        # Header Bar
        #=======================================================================
        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "HeaderBar example"
        self.set_titlebar(hb)

        #=======================================================================
        # Close Button
        #=======================================================================
        button = Gtk.Button()
        icon = Gio.ThemedIcon(name="mail-send-receive-symbolic")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        button.add(image)
        hb.pack_end(button)
        
        #=======================================================================
        # Left-Right Arrow Box        
        #=======================================================================
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(box.get_style_context(), "linked")
        button = Gtk.Button()
        button.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
        box.add(button)
        button = Gtk.Button()
        button.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))
        box.add(button)
        hb.pack_start(box)
        
        self.add(Gtk.TextView())
        

if __name__ == '__main__':
    print('Starting...\n')
    
    win = HeaderBarWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
        
    print('\nDone.')
    

# end of file
