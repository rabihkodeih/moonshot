import gi
from constants import GNOME_ICON_THEME_SYMBOLIC
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio


class SymbolicThemeWindow(Gtk.Window):

    def create_listbox(self):
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        for icon_label in GNOME_ICON_THEME_SYMBOLIC:
            row = Gtk.ListBoxRow()
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
            row.add(hbox)
            label = Gtk.Label(icon_label, xalign=0, selectable=True)
            hbox.pack_start(label, True, True, 0)
            icon = Gio.ThemedIcon(name=icon_label)
            image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.LARGE_TOOLBAR)
            hbox.pack_start(image, False, True, 0)
            listbox.add(row)
        return listbox
    
    def __init__(self):
        Gtk.Window.__init__(self, title="gnome-icon-theme-symbolic theme")
        self.set_border_width(10)
        self.set_default_size(400, 600)
        container = Gtk.ScrolledWindow()
        container.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        listbox = self.create_listbox()
        container.add_with_viewport(listbox)
        self.add(container)


def launch_main():
    win = SymbolicThemeWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()


if __name__ == '__main__':
    print('Starting...\n')

    launch_main()
        
    print('\nDone.')
    

# end of file
