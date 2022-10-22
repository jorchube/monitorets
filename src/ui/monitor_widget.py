from gi.repository import Adw
from gi.repository import Gtk

from .graph_area import GraphArea


class MonitorWidget(Adw.Bin):
    def __init__(self, title, sampler, type, color=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add_css_class("card")
        self.add_css_class("frame")

        title_label = self._build_title_label(title, color)
        drawing_area = self._build_drawing_area()

        self._sampler = sampler
        self._graph_area = self._build_graph_area(drawing_area, color, sampler.sampling_frequency_seconds)
        self._sampler.install_new_sample_callback(self._graph_area.add_value)
        self._overlay = Gtk.Overlay()
        self._overlay.set_child(drawing_area)
        self._overlay.add_overlay(title_label)
        self.set_child(self._overlay)

    def start_sampling(self):
        self._sampler.start()

    def stop_sampling(self):
        self._sampler.stop()

    def _build_title_label(self, title, color):
        label = Gtk.Label()
        label.set_markup(f"<span weight='bold' color='#{color.HTML}'>{title}</span>")
        return label

    def _build_drawing_area(self):
        drawing_area = Gtk.DrawingArea()
        drawing_area.set_hexpand(True)
        drawing_area.set_vexpand(True)

        return drawing_area

    def _build_graph_area(self, drawing_area, color, sampling_frequency_seconds):
        return GraphArea(drawing_area, color, sampling_frequency_seconds)
