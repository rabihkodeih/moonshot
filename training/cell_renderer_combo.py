'''
Created on Dec 3, 2018

@author: rabihkodeih
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class CellRendererComboWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="CellRendererCombo Example")

        self.set_default_size(200, 200)

        liststore_manufacturers = Gtk.ListStore(str)
        manufacturers = ["Sony", "LG",
            "Panasonic", "Toshiba", "Nokia", "Samsung"]
        for item in manufacturers:
            liststore_manufacturers.append([item])

        self.liststore_hardware = Gtk.ListStore(str, str)
        self.liststore_hardware.append(["Television", "Samsung"])
        self.liststore_hardware.append(["Mobile Phone", "LG"])
        self.liststore_hardware.append(["DVD Player", "Sony"])

        # tree view
        treeview = Gtk.TreeView(model=self.liststore_hardware)
        self.add(treeview)
        
        # column 1        
        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("Text", renderer_text, text=0)
        treeview.append_column(column_text)

        # column 2
        renderer_combo = Gtk.CellRendererCombo()
        renderer_combo.set_property("editable", True)
        renderer_combo.set_property("model", liststore_manufacturers)
        renderer_combo.set_property("text-column", 0)
        renderer_combo.set_property("has-entry", False)
        renderer_combo.connect("edited", self.on_combo_changed)
        column_combo = Gtk.TreeViewColumn("Combo", renderer_combo, text=1)
        treeview.append_column(column_combo)


    def on_combo_changed(self, widget, path, text):
        self.liststore_hardware[path][1] = text


if __name__ == '__main__':
    print('Starting...\n')
    
    win = CellRendererComboWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
        
    print('\nDone.')
    

# end of file
