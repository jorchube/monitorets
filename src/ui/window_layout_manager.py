from gi.repository import Gtk
from ..event_broker import EventBroker
from .. import events
from ..preferences import Preferences
from ..preference_keys import PreferenceKeys
from ..layout import Layout


class WindowLayoutManager:
    _WIDTH_HEIGHT_RATIO_THRESHOLD = 1.5

    def __init__(self, window, set_horizontal_layout_callback, set_vertical_layout_callback):
        self._window = window
        self._set_horizontal_layout = set_horizontal_layout_callback
        self._set_vertical_layout = set_vertical_layout_callback

        self._paintable = Gtk.WidgetPaintable()
        self._paintable.set_widget(self._window)

        self._adaptive_layout_enabled = False

        self._layout_selected_callbacks = {
            Layout.ADAPTIVE: self._adaptive_layout_selected,
            Layout.HORIZONTAL: self._horizontal_layout_selected,
            Layout.VERTICAL: self._vertical_layout_selected
        }

        EventBroker.subscribe(events.PREFERENCES_CHANGED, self._on_preferences_changed)

        self._paintable.connect("invalidate-size", self._size_changed)

        self._set_initial_layout()

    def _set_initial_layout(self):
        layout = Preferences.get(PreferenceKeys.LAYOUT)
        if layout == Layout.ADAPTIVE:
            self._adaptive_layout_enabled = True
        else:
            self._layout_selected_callbacks[layout]()

    def _refresh_layout_from_preferences(self):
        layout = Preferences.get(PreferenceKeys.LAYOUT)
        self._layout_selected_callbacks[layout]()

    def _on_preferences_changed(self, preference_key, value):
        if preference_key == PreferenceKeys.LAYOUT:
            self._refresh_layout_from_preferences()

    def _size_changed(self, *args, **kwargs):
        self._evaluate_layout()

    def _evaluate_layout(self):
        if self._adaptive_layout_enabled is False:
            return

        new_width = self._window.get_width()
        new_height = self._window.get_height()

        if self._should_trigger_horizontal_layout(new_width, new_height, self._WIDTH_HEIGHT_RATIO_THRESHOLD):
            self._set_horizontal_layout()

        if self._should_trigger_vertical_layout(new_width, new_height, self._WIDTH_HEIGHT_RATIO_THRESHOLD):
            self._set_vertical_layout()

    def _should_trigger_horizontal_layout(self, width, height, sensibility):
        return (width / height) > sensibility

    def _should_trigger_vertical_layout(self, width, height, sensibility):
        return (height / width) > sensibility

    def _adaptive_layout_selected(self):
        self._adaptive_layout_enabled = True
        self._evaluate_layout()

    def _horizontal_layout_selected(self):
        self._adaptive_layout_enabled = False
        self._set_horizontal_layout()

    def _vertical_layout_selected(self):
        self._adaptive_layout_enabled = False
        self._set_vertical_layout()
