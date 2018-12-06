'''
Created on Dec 3, 2018

@author: rabihkodeih
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class CellRendererTextWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="CellRendererText Example")

        self.set_default_size(200, 200)

        self.liststore = Gtk.ListStore(str, str)
        self.liststore.append(["Fedora", "http://fedoraproject.org/"])
        self.liststore.append(["Slackware", "http://www.slackware.com/"])
        self.liststore.append(["Sidux", "http://sidux.com/"])

        # tree view
        treeview = Gtk.TreeView(model=self.liststore)

        # cell renderers
        c1_renderer_text = Gtk.CellRendererText()
        c2_renderer_editabletext = Gtk.CellRendererText()
        c2_renderer_editabletext.set_property("editable", True)
        c2_renderer_editabletext.connect("edited", self.text_edited)
        
        # column 1        
        column_text = Gtk.TreeViewColumn("Text", c1_renderer_text, text=0)
        treeview.append_column(column_text)
        
        # column 2
        column_editabletext = Gtk.TreeViewColumn("Editable Text", c2_renderer_editabletext, text=1)
        treeview.append_column(column_editabletext)

        self.add(treeview)

    def text_edited(self, widget, path, text):
        self.liststore[path][1] = text


if __name__ == '__main__':
    print('Starting...\n')
    
    win = CellRendererTextWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
        
    print('\nDone.')
    

# end of file
