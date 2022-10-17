from gi.repository import Adw, GObject

from .preferences import Preferences
from .event_broker import EventBroker
from . import events


class Theme:
    SYSTEM = "system"
    DARK = "dark"
    LIGHT = "light"


class Theming:
    _color_scheme_map = {
        Theme.SYSTEM: Adw.ColorScheme.DEFAULT,
        Theme.DARK: Adw.ColorScheme.FORCE_DARK,
        Theme.LIGHT: Adw.ColorScheme.FORCE_LIGHT,
    }

    _PREFERENCES_KEY = "general.theme"

    @classmethod
    def initialize(self):
        self._manager = Adw.StyleManager.get_default()
        self._refresh_theme_from_preferences()

        EventBroker.subscribe(events.THEME_CHANGE_REQUESTED, self._on_theme_change_request)
        EventBroker.subscribe(events.PREFERENCES_CHANGED, self._on_preferences_changed)

    @classmethod
    def _refresh_theme_from_preferences(self):
        theme = Preferences.get("general.theme")
        color_scheme = self._color_scheme_map[theme]
        GObject.idle_add(self._manager.set_color_scheme, color_scheme)
        EventBroker.notify(events.THEME_CHANGED, theme)

    @classmethod
    def _on_theme_change_request(self, theme):
        Preferences.set(self._PREFERENCES_KEY, theme)

    @classmethod
    def _on_preferences_changed(self, preference_key, value):
        if preference_key == self._PREFERENCES_KEY:
            self._refresh_theme_from_preferences()
