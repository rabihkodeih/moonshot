'''
Created on Dec 3, 2018

@author: rabihkodeih
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class CellRendererPixbufWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="CellRendererPixbuf Example")

        self.set_default_size(200, 200)

        self.liststore = Gtk.ListStore(str, str)
        self.liststore.append(["New", "document-new"])
        self.liststore.append(["Open", "document-open"])
        self.liststore.append(["Save", "document-save"])

        # tree view
        treeview = Gtk.TreeView(model=self.liststore)

        # column 1
        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("Text", renderer_text, text=0)
        treeview.append_column(column_text)

        # column 2
        renderer_pixbuf = Gtk.CellRendererPixbuf()
        column_pixbuf = Gtk.TreeViewColumn("Image", renderer_pixbuf, icon_name=1)
        treeview.append_column(column_pixbuf)

        self.add(treeview)


if __name__ == '__main__':
    print('Starting...\n')
    
    win = CellRendererPixbufWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
        
    print('\nDone.')
    

# end of file
