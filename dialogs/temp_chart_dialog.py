import app_state
from gi.repository import Gtk
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas
from matplotlib.figure import Figure


class TempChartDialog(Gtk.Dialog):

    def __init__(self, parent):
        self.loc_id, self.name, _, _ = app_state.get_current_location()
        title = 'Historical temperature chart for "%s"' % self.name
        Gtk.Dialog.__init__(self, title, parent, 0, (Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(800, 500)
        self.set_border_width(10)
        self.props.resizable = False
        self.deleted_locations = []
        self.init_components()

    def init_components(self):
        data = app_state.get_historical_temp_data(self.loc_id)[:10]
        self.temp_chart(data)
        self.show_all()

    def temp_chart(self, data):
        container = self.get_content_area()
        figure = Figure(figsize=(5, 4), dpi=100)
        subplot = figure.add_subplot(111)
        temperatures = [float(temp) for temp, _ in data]
        sample_times = [sample_time.strftime('%b %d\n%I %p') for _, sample_time in data[::-1]]
        subplot.plot(sample_times, temperatures, 'bo-', linewidth=0.75)
        ymin = int(min(temperatures)) if temperatures else 0
        ymax = int(max(temperatures) + 1) if temperatures else 0
        subplot.set_ylim([ymin, ymax])
        ax = subplot.axes
        ax.grid(which='major', axis='both', linestyle='--')
        sw = Gtk.ScrolledWindow()
        container.pack_start(sw, True, True, 0)
        canvas = FigureCanvas(figure)
        sw.add_with_viewport(canvas)


# end of file
