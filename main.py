'''
Created on Dec 3, 2018

@author: rabihkodeih
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk  # @UnresolvedImport

if __name__ == '__main__':
    print('Starting...\n')
    
    win = Gtk.Window()
    assert isinstance(win, gi.overrides.Gtk.Window)  # @UndefinedVariable
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    print(type(Gtk))
    Gtk.main()
    
    print('\nDone.')
    

# end of file

#TODO: implement the main test app
#TODO: apply PEP8 formating
