from gi.repository import Adw, Gtk, Pango
from ..graph_area import GraphArea
from ..graph_redraw_tick_manager import GraphRedrawTickManager
from ..bidirectional_clamp_container_widget import BidirectionalClampContainerWidget
from ...preferences import Preferences
from ...preference_keys import PreferenceKeys
from ...event_broker import EventBroker
from ... import events


class MonitorWidget(Adw.Bin):
    _REDRAW_FREQUENCY_SECONDS = 0.1

    def __init__(self, monitor, type, title, color=None, redraw_freq_seconds=_REDRAW_FREQUENCY_SECONDS, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type = type
        self._color = color
        self._monitor = monitor
        self._title = title
        draw_smooth_graph = Preferences.get(PreferenceKeys.SMOOTH_GRAPH)
        self._graph_area = self._graph_area_instance(self._color, redraw_freq_seconds, draw_smooth_graph)

        self.set_size_request(120, 60)

        self._redraw_manager = GraphRedrawTickManager(self._tick, redraw_freq_seconds)

        self._title_label = self._build_title_label()
        self._refresh_title()

        self._clamp_container = BidirectionalClampContainerWidget()
        self._overlay_bin = Adw.Bin()
        self._overlay_bin.add_css_class("card")
        self._overlay = Gtk.Overlay()

        self.set_child(self._clamp_container)
        self._clamp_container.set_child(self._overlay_bin)
        self._overlay_bin.set_child(self._overlay)

        self._overlay.set_child(self._graph_area.get_drawing_area_widget())
        self._overlay.add_overlay(self._title_label)

        self._setup_graph_area_callback()

        EventBroker.subscribe(events.MONITOR_RENAMED, self._on_monitor_renamed)

    def _setup_widget_hierarchy(self):
        self._clamp_container.set_child(self._overlay_bin)
        self._overlay_bin.set_child(self._overlay)
        self.set_child(self._clamp_container)

    def _graph_area_instance(self, color, redraw_freq_seconds, draw_smooth_graph):
        return GraphArea(color, redraw_freq_seconds, smooth_graph=draw_smooth_graph)

    def _on_monitor_renamed(self, monitor_type, name):
        if self._type == monitor_type:
            if name is None:
                self._set_title(self._title)
            else:
                self._set_title(name)

    def start(self):
        self._monitor.start()
        self._redraw_manager.start()

    def stop(self):
        self._monitor.stop()
        self._redraw_manager.stop()

    def _build_title_label(self):
        label = Gtk.Label()
        label.set_margin_start(10)
        label.set_margin_end(10)
        label.set_ellipsize(Pango.EllipsizeMode.MIDDLE)

        return label

    def _refresh_title(self):
        custom_name = Preferences.get_custom_name(self._type)
        if custom_name:
            self._set_title(custom_name)
        else:
            self._set_title(self._title)

    def _set_title(self, title):
        self._title_label.set_markup(f"<span weight='bold' color='#{self._color.HTML}'>{title}</span>")

    def _tick(self):
        self._graph_area.redraw_tick()

    def _setup_graph_area_callback(self):
        self._monitor.install_new_values_callback(self._new_values)

    def _new_values(self, values):
        self._graph_area.set_new_values(values)
