from gi.repository import Gtk
from ..event_broker import EventBroker
from .. import events
from ..preferences import Preferences
from ..preference_keys import PreferenceKeys
from ..layout import Layout


class WindowLayoutManager:
    _WIDTH_HEIGHT_RATIO_THRESHOLD = 1.5

    def __init__(
        self, window, set_horizontal_layout_callback, set_vertical_layout_callback
    ):
        self._window = window
        self._set_horizontal_layout = set_horizontal_layout_callback
        self._set_vertical_layout = set_vertical_layout_callback

        self._paintable = Gtk.WidgetPaintable()
        self._paintable.set_widget(self._window)

        self._layout_selected_callbacks = {
            Layout.HORIZONTAL: self._horizontal_layout_selected,
            Layout.VERTICAL: self._vertical_layout_selected,
        }

        EventBroker.subscribe(events.PREFERENCES_CHANGED, self._on_preferences_changed)

        self._set_initial_layout()

    def _set_initial_layout(self):
        layout = Preferences.get(PreferenceKeys.LAYOUT)
        self._layout_selected_callbacks[layout]()

    def _refresh_layout_from_preferences(self):
        layout = Preferences.get(PreferenceKeys.LAYOUT)
        self._layout_selected_callbacks[layout]()

    def _on_preferences_changed(self, preference_key, value):
        if preference_key == PreferenceKeys.LAYOUT:
            self._refresh_layout_from_preferences()

    def _horizontal_layout_selected(self):
        self._set_horizontal_layout()

    def _vertical_layout_selected(self):
        self._set_vertical_layout()
