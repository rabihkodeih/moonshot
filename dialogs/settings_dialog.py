'''
Created on Dec 9, 2018

@author: rabihkodeih
'''

import app_state
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class SettingsDialog(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Settings", parent, 0,
            (Gtk.STOCK_CANCEL, 
             Gtk.ResponseType.CANCEL,
             Gtk.STOCK_SAVE, 
             Gtk.ResponseType.OK))
        self.set_default_size(320, 400)
        self.set_border_width(10)
        self.props.resizable = False
        self.deleted_locations = []
        self.init_components()
    
    
    def init_components(self):
        container = self.get_content_area()
        
        # labels
        container.pack_start(Gtk.Label('Locations'), False, False, 0)
        help_label = Gtk.Label()
        help_label.set_markup('<span font_size="10240" font_weight="light">double click any cell to edit</span>')
        container.pack_start(help_label, False, False, 0)
        
        # tree view
        self.treeview_container = Gtk.ScrolledWindow()
        self.treeview_container.set_vexpand(True)
        locations = app_state.get_locations()
        self.store = Gtk.ListStore(str, str, str, str)
        for loc in locations:
            self.store.append(loc)
        self.treeview = Gtk.TreeView(model=self.store)
        for i, column_title in enumerate(["Id", "Location Name", "Latitude", "Longitude"]):
            renderer = Gtk.CellRendererText()
            if i == 0:
                column = Gtk.TreeViewColumn(column_title, renderer, text=i)
                column.props.visible = False
            else:
                renderer.props.editable = True
                renderer.connect("edited", self.text_edited_handler(i))
                column = Gtk.TreeViewColumn(column_title, renderer, text=i)
                column.set_min_width(50)
                column.set_sizing(Gtk.TreeViewColumnSizing.AUTOSIZE)
                column.set_resizable(True)
            self.treeview.append_column(column)
        self.treeview_container.add(self.treeview)       
        container.pack_start(self.treeview_container, True, True, 10)
        
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
    
    def text_edited_handler(self, column_index):
        def text_edited(widget, path, text):
            self.store[path][column_index] = text
        return text_edited
    
    def add_button_clicked(self, widget):
        new_loation_model = ('-1', '_name_', '_lat_', '_long_') 
        self.store.append(new_loation_model)
    
    def delete_button_clicked(self, widget):
        selection = self.treeview.get_selection()
        model, paths = selection.get_selected_rows()
        self.deleted_locations.append(list(self.store[paths[0]]))
        for path in paths:
            model.remove(model.get_iter(path))
    
    def save_settings(self):
        locations = list(self.store)
        app_state.save_locations(locations, self.deleted_locations)
        

# end of file
