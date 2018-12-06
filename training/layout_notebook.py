'''
Created on Dec 3, 2018

@author: rabihkodeih
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Simple Notebook Example")
        self.set_border_width(3)

        #=======================================================================
        # Notebook
        #=======================================================================
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        #=======================================================================
        # Tab 1
        #=======================================================================
        self.page1 = Gtk.Box()
        self.page1.set_border_width(10)
        self.page1.add(Gtk.Label('Default Page!'))
        self.notebook.append_page(self.page1, Gtk.Label('Plain Title'))

        #=======================================================================
        # Tab 2
        #=======================================================================
        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        self.page2.add(Gtk.Label('A page with an image for a Title.'))
        self.notebook.append_page(
            self.page2,
            Gtk.Image.new_from_icon_name(
                "help-about",
                Gtk.IconSize.MENU
            )
        )


if __name__ == '__main__':
    print('Starting...\n')
    
    win = MyWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
        
    print('\nDone.')
    

# end of file
