from ..event_broker import EventBroker
from .. import events
from ..preferences import Preferences
from ..theming import Theme


class ThemeToggleManager:
    def __init__(self, preferences_box):
        self._preference_key = "general.theme"
        self._theme_to_toggle_button_map = {
            Theme.SYSTEM: None,
            Theme.LIGHT: None,
            Theme.DARK: None,
        }

        self._preferences_box = preferences_box

        self._theme_to_toggle_button_map[Theme.SYSTEM] = self._preferences_box._system_theme_toggle_button
        self._theme_to_toggle_button_map[Theme.LIGHT] = self._preferences_box._light_theme_toggle_button
        self._theme_to_toggle_button_map[Theme.DARK] = self._preferences_box._dark_theme_toggle_button

        self._preferences_box._system_theme_toggle_button.connect("clicked", self._on_system_theme_button_clicked)
        self._preferences_box._light_theme_toggle_button.connect("clicked", self._on_light_theme_button_clicked)
        self._preferences_box._dark_theme_toggle_button.connect("clicked", self._on_dark_theme_button_clicked)

        theme = Preferences.get(self._preference_key)
        self._set_active_toggle_for_theme(theme)

        EventBroker.subscribe(events.PREFERENCES_CHANGED, self._on_preference_changed)

    def _on_system_theme_button_clicked(self, user_data):
        Preferences.set(self._preference_key, Theme.SYSTEM)

    def _on_light_theme_button_clicked(self, user_data):
        Preferences.set(self._preference_key, Theme.LIGHT)

    def _on_dark_theme_button_clicked(self, user_data):
        Preferences.set(self._preference_key, Theme.DARK)

    def _set_active_toggle_for_theme(self, theme):
        self._theme_to_toggle_button_map[theme].set_active(True)

    def _on_preference_changed(self, preference_key, value):
        if preference_key == self._preference_key:
            self._set_active_toggle_for_theme(value)
