from gi.repository import Gtk, GObject

from .monitor_widget import MonitorWidget
from .graph_area import GraphArea
from .graph_redraw_tick_manager import GraphRedrawTickManager


class GraphMonitorWidget(MonitorWidget):

    _REDRAW_FREQUENCY_HZ = 10

    def __init__(self, title, sampler, color=None, *args, **kwargs):
        super().__init__(title, sampler, *args, **kwargs)

        self.set_size_request(120, 40)

        self._redraw_frequency_seconds = 1.0/self._REDRAW_FREQUENCY_HZ
        self._redraw_manager = GraphRedrawTickManager(self._tick, self._redraw_frequency_seconds)

        self.add_css_class("card")
        self.add_css_class("frame")

        self._sampler = sampler
        title_label = self._build_title_label(title, color)
        drawing_area = self._build_drawing_area()

        self._graph_area = self._build_graph_area(drawing_area, color, self._redraw_frequency_seconds)
        self._sampler.install_new_sample_callback(self._graph_area.add_value)

        self._overlay = Gtk.Overlay()
        self._overlay.set_child(drawing_area)
        self._overlay.add_overlay(title_label)
        self.set_child(self._overlay)


    def start(self):
        self._redraw_manager.start()
        self._sampler.start()

    def stop(self):
        self._sampler.stop()
        self._redraw_manager.stop()

    def _tick(self):
        GObject.idle_add(self._graph_area.tick)

    def _build_title_label(self, title, color):
        label = Gtk.Label()
        label.set_markup(f"<span weight='bold' color='#{color.HTML}'>{title}</span>")
        return label

    def _build_drawing_area(self):
        drawing_area = Gtk.DrawingArea()
        drawing_area.set_hexpand(True)
        drawing_area.set_vexpand(True)

        return drawing_area

    def _build_graph_area(self, drawing_area, color, redraw_frequency_seconds):
        return GraphArea(drawing_area, color, redraw_frequency_seconds)
