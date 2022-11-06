from gi.repository import Adw, GObject

from .preferences import Preferences
from .preference_keys import PreferenceKeys
from .event_broker import EventBroker
from . import events
from .theme import Theme


class Theming:
    _color_scheme_map = {
        Theme.SYSTEM: Adw.ColorScheme.DEFAULT,
        Theme.DARK: Adw.ColorScheme.FORCE_DARK,
        Theme.LIGHT: Adw.ColorScheme.FORCE_LIGHT,
    }

    @classmethod
    def initialize(self):
        self._manager = Adw.StyleManager.get_default()
        self._refresh_theme_from_preferences()

        EventBroker.subscribe(events.PREFERENCES_CHANGED, self._on_preferences_changed)

    @classmethod
    def _refresh_theme_from_preferences(self):
        theme = Preferences.get("general.theme")
        color_scheme = self._color_scheme_map[theme]
        GObject.idle_add(self._manager.set_color_scheme, color_scheme)

    @classmethod
    def _on_preferences_changed(self, preference_key, value):
        if preference_key == PreferenceKeys.THEME:
            self._refresh_theme_from_preferences()
