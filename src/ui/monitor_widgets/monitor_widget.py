from gi.repository import Adw, Gtk
from ..graph_area import GraphArea
from ..graph_redraw_tick_manager import GraphRedrawTickManager


class MonitorWidget(Adw.Bin):
    _REDRAW_FREQUENCY_SECONDS = 0.1

    def __init__(self, monitor, title, color=None, redraw_freq_seconds=_REDRAW_FREQUENCY_SECONDS, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._monitor = monitor
        self._graph_area = self._graph_area_instance(self._color, redraw_freq_seconds)

        self.set_size_request(120, 40)

        self._redraw_manager = GraphRedrawTickManager(self._tick, redraw_freq_seconds)

        self.add_css_class("card")
        self.add_css_class("frame")

        title_label = self._build_title_label(title, color)

        self._overlay = Gtk.Overlay()
        self._overlay.set_child(self._graph_area.get_drawing_area_widget())
        self._overlay.add_overlay(title_label)
        self.set_child(self._overlay)

        self._setup_graph_area_callback()

    def _graph_area_instance(self, color, redraw_freq_seconds):
        return GraphArea(color, redraw_freq_seconds)

    def start(self):
        self._monitor.start()
        self._redraw_manager.start()

    def stop(self):
        self._monitor.stop()
        self._redraw_manager.stop()

    def _build_title_label(self, title, color):
        label = Gtk.Label()
        label.set_markup(f"<span weight='bold' color='#{color.HTML}'>{title}</span>")
        return label

    def _tick(self):
        self._graph_area.redraw_tick()

    def _setup_graph_area_callback(self):
        self._monitor.install_new_values_callback(self._new_values)

    def _new_values(self, values):
        self._graph_area.set_new_values(values)
