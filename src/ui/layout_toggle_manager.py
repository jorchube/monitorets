from ..layout import Layout
from ..preferences import Preferences
from ..preference_keys import PreferenceKeys
from ..event_broker import EventBroker
from .. import events


class LayoutToggleManager:

    def __init__(self, preferences_box):
        self._layout_to_toggle_button_map = {
            Layout.ADAPTIVE: None,
            Layout.HORIZONTAL: None,
            Layout.VERTICAL: None,
        }

        self._preferences_box = preferences_box

        self._layout_to_toggle_button_map[Layout.ADAPTIVE] = self._preferences_box._adaptive_layout_toggle_button
        self._layout_to_toggle_button_map[Layout.HORIZONTAL] = self._preferences_box._horizontal_layout_toggle_button
        self._layout_to_toggle_button_map[Layout.VERTICAL] = self._preferences_box._vertical_layout_toggle_button

        self._preferences_box._adaptive_layout_toggle_button.connect("clicked", self._on_adaptive_layout_button_clicked)
        self._preferences_box._horizontal_layout_toggle_button.connect("clicked", self._on_horizontal_layout_button_clicked)
        self._preferences_box._vertical_layout_toggle_button.connect("clicked", self._on_vertical_layout_button_clicked)

        EventBroker.subscribe(events.PREFERENCES_CHANGED, self._on_preference_changed)

        layout = Preferences.get(PreferenceKeys.LAYOUT)
        self._set_active_toggle_for_layout(layout)

    def _on_adaptive_layout_button_clicked(self, user_data):
        Preferences.set(PreferenceKeys.LAYOUT, Layout.ADAPTIVE)

    def _on_horizontal_layout_button_clicked(self, user_data):
        Preferences.set(PreferenceKeys.LAYOUT, Layout.HORIZONTAL)

    def _on_vertical_layout_button_clicked(self, user_data):
        Preferences.set(PreferenceKeys.LAYOUT, Layout.VERTICAL)

    def _set_active_toggle_for_layout(self, layout):
        self._layout_to_toggle_button_map[layout].set_active(True)

    def _on_preference_changed(self, key, value):
        if key == PreferenceKeys.LAYOUT:
            self._set_active_toggle_for_layout(value)
