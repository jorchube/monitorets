from gi.repository import Gtk
from ..event_broker import EventBroker
from .. import events
from ..preferences import Preferences
from ..preference_keys import PreferenceKeys
from ..layout import Layout
from .. import monitor_descriptors
from math import ceil


class WindowLayoutManager:
    @classmethod
    def initialize(self):
        self._monitors_flow_box = Gtk.FlowBox()
        self._monitors_flow_box.set_row_spacing(5)
        self._monitors_flow_box.set_column_spacing(5)
        self._num_monitors = 0

        self._layout_selected_callbacks = {
            Layout.HORIZONTAL: self._horizontal_layout_selected,
            Layout.VERTICAL: self._vertical_layout_selected,
            Layout.GRID: self._grid_layout_selected,
        }

        EventBroker.subscribe(events.PREFERENCES_CHANGED, self._on_preferences_changed)

        self._refresh_layout_from_preferences()
        self._monitors_flow_box.set_sort_func(self._sort_function, None, None)

    @classmethod
    def add_monitor(self, monitor):
        self._monitors_flow_box.append(monitor)
        self._num_monitors += 1
        self._refresh_grid_row_limit()

    @classmethod
    def remove_monitor(self, monitor):
        self._monitors_flow_box.remove(monitor)
        self._num_monitors -= 1
        self._refresh_grid_row_limit()

    @classmethod
    def _refresh_grid_row_limit(self):
        layout = Preferences.get(PreferenceKeys.LAYOUT)
        if layout in [Layout.HORIZONTAL, Layout.VERTICAL]:
            self._set_grid_row_limit(1)
            return
        self._set_grid_row_limit(ceil(self._num_monitors / 3))

    @classmethod
    def _set_grid_row_limit(self, value):
        self._monitors_flow_box.set_max_children_per_line(value)
        self._monitors_flow_box.set_min_children_per_line(value)

    @classmethod
    def get_container_widget(self):
        return self._monitors_flow_box

    @classmethod
    def _refresh_layout_from_preferences(self):
        layout = Preferences.get(PreferenceKeys.LAYOUT)
        self._layout_selected_callbacks[layout]()

    @classmethod
    def _on_preferences_changed(self, preference_key, value):
        if preference_key == PreferenceKeys.LAYOUT:
            self._refresh_layout_from_preferences()

    @classmethod
    def _horizontal_layout_selected(self):
        self._monitors_flow_box.set_orientation(Gtk.Orientation.VERTICAL)
        self._refresh_grid_row_limit()

    @classmethod
    def _vertical_layout_selected(self):
        self._monitors_flow_box.set_orientation(Gtk.Orientation.HORIZONTAL)
        self._refresh_grid_row_limit()

    @classmethod
    def _grid_layout_selected(self):
        self._monitors_flow_box.set_orientation(Gtk.Orientation.HORIZONTAL)
        self._refresh_grid_row_limit()

    @classmethod
    def _sort_function(self, flow_box_child_1, flow_box_child_2, *_):
        monitor_1 = flow_box_child_1.get_child()
        monitor_2 = flow_box_child_2.get_child()

        ordering_dict = monitor_descriptors.get_ordering_dict()
        monitor_1_order = ordering_dict[monitor_1.type]
        monitor_2_order = ordering_dict[monitor_2.type]
        return monitor_1_order - monitor_2_order
