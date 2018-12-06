'''
Created on Dec 3, 2018

@author: rabihkodeih
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self, title='CM')
        self.set_border_width(10)
        # set default size
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.add(listbox)
        
        # Checkbox
        row_1 = Gtk.ListBoxRow()
        box_1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row_1.add(box_1)
        label = Gtk.Label("Check if you love CBs")
        check = Gtk.CheckButton()
        box_1.pack_start(label, False, True, 0)
        box_1.pack_start(check, True, True, 50)
        listbox.add(row_1)

        # Checkbox
        row_2 = Gtk.ListBoxRow()
        box_2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row_2.add(box_2)
        label = Gtk.Label("B making machine")
        switch = Gtk.Switch()
        box_2.pack_start(label, False, True, 0)
        box_2.pack_start(switch, True, True, 0)
        listbox.add(row_2)
        

def launch_main_window():
    win = MainWindow()
    # win.connect("destroy", Gtk.main_quit)
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()


if __name__ == '__main__':
    print('Starting...\n')
    
    
    
    from pprint import pprint
    import requests
    r = requests.get()
    pprint(r.json())
    
        
    print('\nDone.')
    

# end of file

#TODO: login into soshace mail and check message, document all important info of sochace into dropbox

# Specs: implement the main test app using the following specs:
# Locations
# Display weather for at least 24 hours ahead
# refresh/update for weather data
# keep historical records
# use history to provide temperature chart

# API:
# api.openweathermap.org/data/2.5/weather?q={city name}
# api.openweathermap.org/data/2.5/weather?q={city name},{country code}
# api.openweathermap.org/data/2.5/weather?id={city_id}
# api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}
# api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}
# JSON response (Only really measured or calculated data is displayed in API response):
# weather condition codes: https://openweathermap.org/weather-conditions



#TODO: apply PEP8 formating








