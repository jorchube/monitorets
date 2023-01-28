from gi.repository import Gtk
from ..event_broker import EventBroker
from .. import events
from ..preferences import Preferences
from ..preference_keys import PreferenceKeys
from ..layout import Layout


class WindowLayoutManager:
    @classmethod
    def initialize(self):
        self._monitors_flow_box = Gtk.FlowBox()
        self._monitors_flow_box.set_max_children_per_line(1)
        self._monitors_flow_box.set_row_spacing(5)
        self._monitors_flow_box.set_column_spacing(5)

        self._layout_selected_callbacks = {
            Layout.HORIZONTAL: self._horizontal_layout_selected,
            Layout.VERTICAL: self._vertical_layout_selected,
        }

        EventBroker.subscribe(events.PREFERENCES_CHANGED, self._on_preferences_changed)

        self._refresh_layout_from_preferences()

    @classmethod
    def add_monitor(self, monitor):
        self._monitors_flow_box.append(monitor)

    @classmethod
    def remove_monitor(self, monitor):
        self._monitors_flow_box.remove(monitor)

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

    @classmethod
    def _vertical_layout_selected(self):
        self._monitors_flow_box.set_orientation(Gtk.Orientation.HORIZONTAL)
