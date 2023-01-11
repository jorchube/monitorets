from ..layout import Layout
from ..preferences import Preferences
from ..preference_keys import PreferenceKeys
from ..event_broker import EventBroker
from .. import events


class LayoutToggleManager:

    def __init__(self, preferences_page):
        self._layout_to_toggle_button_map = {
            Layout.HORIZONTAL: None,
            Layout.VERTICAL: None,
        }

        self._preferences_page = preferences_page

        self._layout_to_toggle_button_map[Layout.HORIZONTAL] = self._preferences_page._horizontal_check_button
        self._layout_to_toggle_button_map[Layout.VERTICAL] = self._preferences_page._vertical_check_button

        self._preferences_page._vertical_check_button.connect("toggled", self._on_vertical_check_button_toggled)
        self._preferences_page._horizontal_check_button.connect("toggled", self._on_horizontal_check_button_toggled)

        EventBroker.subscribe(events.PREFERENCES_CHANGED, self._on_preference_changed)

        layout = Preferences.get(PreferenceKeys.LAYOUT)
        self._set_active_toggle_for_layout(layout)

    def _set_active_toggle_for_layout(self, layout):
        self._layout_to_toggle_button_map[layout].set_active(True)

    def _on_vertical_check_button_toggled(self, toggle_button):
        if toggle_button.get_active():
            Preferences.set(PreferenceKeys.LAYOUT, Layout.VERTICAL)

    def _on_horizontal_check_button_toggled(self, toggle_button):
        if toggle_button.get_active():
            Preferences.set(PreferenceKeys.LAYOUT, Layout.HORIZONTAL)

    def _on_preference_changed(self, key, value):
        if key == PreferenceKeys.LAYOUT:
            self._set_active_toggle_for_layout(value)
