'''
Created on Dec 3, 2018

@author: rabihkodeih
'''


from components.weather_info_widget import WeatherInfoWidget
from components.weather_day_widget import WeatherDayWidget
from components.weather_week_widget import WeatherWeekWidget
from dialogs.settings_dialog import SettingsDialog

import app_state
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, GObject


class MainWindow(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self, title='CM')
        self.weather_info_widget = None
        self.weather_day_widget = None
        self.weather_week_widget = None
        self.init_components()
    
    def init_components(self):
        # window initialization
        self.set_border_width(10)
        self.set_default_size(400, 600)
        self.props.resizable = False
        self.main_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.main_container)
        # header bar
        self.header_bar = self.create_header_bar()
        self.set_titlebar(self.header_bar)
        # location selector
        self.location_selector = self.create_location_selector()
        self.main_container.pack_start(self.location_selector, False, True, 10)
        # weather info widget
        self.weather_info_widget = WeatherInfoWidget()
        self.main_container.pack_start(self.weather_info_widget, True, True, 10)
        # weather day widget
        self.weather_day_widget = WeatherDayWidget()
        self.main_container.pack_start(self.weather_day_widget, False, True, 50)
        # weathe week widget
        self.weather_week_widget = WeatherWeekWidget()
        self.main_container.pack_start(self.weather_week_widget, False, True, 10)

    def create_header_bar(self):
        hb = Gtk.HeaderBar()
        hb.set_decoration_layout("menu:close")
        hb.set_show_close_button(True)
        hb.props.title = "Moonshot"
        # refresh button
        refresh_btn = Gtk.Button.new_from_icon_name("view-refresh-symbolic", Gtk.IconSize.BUTTON)
        refresh_btn.connect("clicked", lambda _: self.emit('update_app_state'))
        hb.pack_start(refresh_btn)
        # temperature chart button
        tmpchart_btn = Gtk.Button.new_from_icon_name("utilities-system-monitor-symbolic", Gtk.IconSize.BUTTON)
        hb.pack_start(tmpchart_btn)
        # settings button
        settings_btn = Gtk.Button.new_from_icon_name("emblem-system-symbolic", Gtk.IconSize.BUTTON)
        settings_btn.connect('clicked', self.settings_btn_clicked)
        hb.pack_start(settings_btn)
        return hb

    def settings_btn_clicked(self, widget):  # @UnusedVariable
        settings_dialog = SettingsDialog(self)
        response = settings_dialog.run()
        if response == Gtk.ResponseType.OK:
            settings_dialog.save_settings()
            self.location_selector.remove(self.location_selector.combo)
            self.create_locations_combobox(self.location_selector)
            self.location_selector.show_all()
        settings_dialog.destroy()

    def create_locations_combobox(self, container):
        combo = Gtk.ComboBoxText()
        container.combo = combo
        container.pack_start(combo, True, False, 0)
        for location_id, name, _ in app_state.get_locations():
            combo.append(location_id, name)
        location_id = app_state.get_current_location_id()
        location_ids = set(l[0] for l in app_state.get_locations())
        if location_id not in location_ids:
            location_id = location_ids.pop()
        combo.connect("changed", self.location_selector_combo_changed)
        combo.set_active_id(location_id)
        return combo

    def create_location_selector(self):
        box = Gtk.Box()
        self.create_locations_combobox(box)
        return box

    def location_selector_combo_changed(self, combo):
        print('combo changed')
        location_id = combo.get_active_id()
        app_state.set_current_location(location_id)
        self.emit('update_app_state')

    @GObject.Signal
    def update_app_state(self):
        app_state.async_update(self)
        
    @GObject.Signal    
    def refresh(self):
        self.weather_info_widget.emit('refresh')
        self.weather_day_widget.emit('refresh')
        self.weather_week_widget.emit('refresh')

      
def app_main():
    win = MainWindow()
    win.emit('refresh')
    win.connect("destroy", Gtk.main_quit)
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()

    

if __name__ == '__main__':
    print('Starting...\n')
    
    app_main()
    Gtk.main()

    print('\nDone.')
    

# end of file



# SPECS:
# Locations (1+)
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



#TODO: https://stackoverflow.com/questions/19452797/draw-a-svg-image-in-gtk3-from-svg-source-in-python
#TODO: apply PEP8 formating
#TODO: add documentation where it counts








