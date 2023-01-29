import math
from gi.repository import Adw, Gtk, Pango, GObject
from ..graph_area import GraphArea
from ..graph_redraw_tick_manager import GraphRedrawTickManager
from ...preferences import Preferences
from ...preference_keys import PreferenceKeys
from ...event_broker import EventBroker
from ... import events
from ..monitor_title_overlay import MonitorTitleOverlay


class MonitorWidget(Adw.Bin):
    _REDRAW_FREQUENCY_SECONDS = 0.1
    _WIDTH_PER_SAMPLE = 10

    def __init__(
        self,
        monitor,
        type,
        title,
        color=None,
        redraw_freq_seconds=_REDRAW_FREQUENCY_SECONDS,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self._type = type
        self._color = color
        self._monitor = monitor
        self._title = title
        self._show_current_value_label = Preferences.get(
            PreferenceKeys.SHOW_CURRENT_VALUE
        )

        draw_smooth_graph = Preferences.get(PreferenceKeys.SMOOTH_GRAPH)
        self._graph_area = self._graph_area_instance(
            self._color, redraw_freq_seconds, draw_smooth_graph
        )
        self._graph_area.set_width_per_sample(self._WIDTH_PER_SAMPLE)

        self.set_size_request(120, 65)

        self._redraw_manager = GraphRedrawTickManager(self._tick, redraw_freq_seconds)

        self._overlay_bin = Adw.Bin()
        self._overlay_bin.add_css_class("card")
        self._overlay = Gtk.Overlay()

        self.set_child(self._overlay_bin)
        self._overlay_bin.set_child(self._overlay)

        self._overlay.set_child(self._graph_area.get_drawing_area_widget())

        self._monitor_title_overlay = MonitorTitleOverlay(self._color.HTML)
        self._overlay.add_overlay(self._monitor_title_overlay)
        self._refresh_title()

        self._setup_graph_area_callback()

        EventBroker.subscribe(events.MONITOR_RENAMED, self._on_monitor_renamed)
        EventBroker.subscribe(events.PREFERENCES_CHANGED, self._on_preference_changed)

        self._paintable = Gtk.WidgetPaintable()
        self._paintable.set_widget(self)
        self._paintable.connect("invalidate-size", self._on_size_changed)

    @property
    def type(self):
        return self._type

    def _graph_area_instance(self, color, redraw_freq_seconds, draw_smooth_graph):
        return GraphArea(color, redraw_freq_seconds, smooth_graph=draw_smooth_graph)

    def _on_monitor_renamed(self, monitor_type, name):
        if self._type == monitor_type:
            if name is None:
                self._set_title(self._title)
            else:
                self._set_title(name)

    def _on_preference_changed(self, key, value):
        if key == PreferenceKeys.SHOW_CURRENT_VALUE:
            self._on_show_current_value_changed(value)

    def _on_show_current_value_changed(self, new_value):
        self._show_current_value_label = new_value

    def start(self):
        self._monitor.start()
        self._redraw_manager.start()

    def stop(self):
        self._monitor.stop()
        self._redraw_manager.stop()

    def _set_value_label(self, value):
        self._monitor_title_overlay.set_value(value)

    def _refresh_title(self):
        custom_name = Preferences.get_custom_name(self._type)
        if custom_name:
            self._set_title(custom_name)
        else:
            self._set_title(self._title)

    def _set_title(self, title):
        self._monitor_title_overlay.set_title(title)

    def _tick(self):
        self._graph_area.redraw_tick()

    def _setup_graph_area_callback(self):
        self._monitor.install_new_values_callback(self._new_values)

    def _new_values(self, values, readable_value=None):
        if self._show_current_value_label:
            self._set_value_label(readable_value)
        else:
            self._set_value_label(None)

        self._graph_area.set_new_values(values)

    def _on_size_changed(self, paintable):
        new_width = self.get_width()
        self._set_max_stored_samples_for_width(new_width)

    def _set_max_stored_samples_for_width(self, width):
        num_needed_samples = self._calculate_needed_samples_for_width(width)
        self._monitor.set_max_number_of_stored_samples(num_needed_samples)

    def _calculate_needed_samples_for_width(self, width):
        num_samples = math.ceil(width / self._WIDTH_PER_SAMPLE)
        return num_samples
