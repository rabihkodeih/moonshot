'''
Created on Dec 9, 2018

@author: rabihkodeih
'''

import app_state
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gio


class SettingsDialog(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Settings", parent, 0,
            (Gtk.STOCK_CANCEL, 
             Gtk.ResponseType.CANCEL,
             Gtk.STOCK_SAVE, 
             Gtk.ResponseType.OK))
        self.set_default_size(300, 400)
        self.set_border_width(10)
        self.props.resizable = False
        self.init_components()
    
    def init_components(self):
        container = self.get_content_area()
        
        # labels
        container.pack_start(Gtk.Label('Locations'), False, False, 0)
        help_label = Gtk.Label()
        help_label.set_markup('<span font_size="10240" font_weight="light">double click any cell to edit</span>')
        container.pack_start(help_label, False, False, 0)
        
        # tree view
        locations = app_state.get_locations()
        self.store = Gtk.ListStore(str, str, str)
        for loc in locations:
            self.store.append(loc)
        self.treeview = Gtk.TreeView(model=self.store)
        for i, column_title in enumerate(["Id", "Location Name", "Coordinates"]):
            renderer = Gtk.CellRendererText()
            if i > 0:
                renderer.props.editable = True
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)
        container.pack_start(self.treeview, True, True, 10)
        
        # action bar
        action_bar = Gtk.ActionBar()
        add_button = Gtk.Button.new_from_icon_name("list-add-symbolic", Gtk.IconSize.LARGE_TOOLBAR)
        add_button.connect('clicked', self.add_button_clicked)
        action_bar.pack_start(add_button)
        delete_button = Gtk.Button.new_from_icon_name("edit-delete-symbolic", Gtk.IconSize.LARGE_TOOLBAR)
        delete_button.connect('clicked', self.delete_button_clicked)
        action_bar.pack_start(delete_button)
        container.pack_end(action_bar, False, False, 5)
        
        self.show_all()
    
    def add_button_clicked(self, _):
        #TODO: on add click: just add a new row to the view with selection and default values
        print('new row added')
        pass
    
    def delete_button_clicked(self, _):
        #TODO: on add click: just add a new row to the view with selection and default values
        print('selected row deleted')
        pass
    
    def save_settings(self):
        #TODO: save new location settings to persistent storage
        pass
        

# end of file