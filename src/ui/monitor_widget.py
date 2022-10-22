from gi.repository import Adw
from gi.repository import Gtk

from .graph_area import GraphArea


class MonitorWidget(Adw.Bin):
    def __init__(self, title, sampler, type, color=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add_css_class("card")
        self.add_css_class("frame")

        self._title = title
        self._sampler = sampler
        self._type = type
        self._color = color
        self._drawing_area = self._build_drawing_area()

        self._overlay = Gtk.Overlay()
        self.set_child(self._overlay)

        self._overlay.set_child(self._drawing_area)

        title = self._build_title_label()
        self._overlay.add_overlay(title)

        self._graph_area = self._build_graph_area()
        self._sampler.install_new_sample_callback(self._graph_area.add_value)

    def start_sampling(self):
        self._sampler.start()

    def stop_sampling(self):
        self._sampler.stop()

    def _build_title_label(self):
        label = Gtk.Label()
        label.set_markup(f"<span weight='bold' color='#{self._color.HTML}'>{self._title}</span>")
        return label

    def _build_drawing_area(self):
        drawing_area = Gtk.DrawingArea()
        drawing_area.set_hexpand(True)
        drawing_area.set_vexpand(True)

        return drawing_area

    def _build_graph_area(self):
        return GraphArea(self._drawing_area, self._color, self._sampler.sampling_frequency_seconds)
