from gi.repository import Adw, Gtk, Pango
from ..graph_area import GraphArea
from ..graph_redraw_tick_manager import GraphRedrawTickManager
from ..bidirectional_clamp_container_widget import BidirectionalClampContainerWidget


class MonitorWidget(Adw.Bin):
    _REDRAW_FREQUENCY_SECONDS = 0.1

    def __init__(self, monitor, title, color=None, redraw_freq_seconds=_REDRAW_FREQUENCY_SECONDS, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._color = color
        self._monitor = monitor
        self._graph_area = self._graph_area_instance(self._color, redraw_freq_seconds)

        self.set_size_request(120, 40)

        self._redraw_manager = GraphRedrawTickManager(self._tick, redraw_freq_seconds)

        title_label = self._build_title_label(title, color)

        self._clamp_container = BidirectionalClampContainerWidget()
        self._overlay_bin = Adw.Bin()
        self._overlay_bin.add_css_class("card")
        self._overlay = Gtk.Overlay()


        self.set_child(self._clamp_container)
        self._clamp_container.set_child(self._overlay_bin)
        self._overlay_bin.set_child(self._overlay)

        self._overlay.set_child(self._graph_area.get_drawing_area_widget())
        self._overlay.add_overlay(title_label)

        self._setup_graph_area_callback()

    def _setup_widget_hierarchy(self):
        self._clamp_container.set_child(self._overlay_bin)
        self._overlay_bin.set_child(self._overlay)
        self.set_child(self._clamp_container)

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
        label.set_margin_start(10)
        label.set_margin_end(10)
        label.set_markup(f"<span weight='bold' color='#{color.HTML}'>{title}</span>")
        label.set_ellipsize(Pango.EllipsizeMode.MIDDLE)

        return label

    def _tick(self):
        self._graph_area.redraw_tick()

    def _setup_graph_area_callback(self):
        self._monitor.install_new_values_callback(self._new_values)

    def _new_values(self, values):
        self._graph_area.set_new_values(values)
