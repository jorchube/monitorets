from gi.repository import Gtk

from ..event_broker import EventBroker
from .. import events
from ..preferences import Preferences


class MonitorEnableSwitch(Gtk.Switch):
    def __init__(self, monitor_type, preference_key, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_valign(Gtk.Align.CENTER)
        self._monitor_type = monitor_type
        self._preference_key = preference_key

        is_active = Preferences.get(self._preference_key)
        self.set_active(is_active)

        self.connect("state-set", self._on_state_changed)
        EventBroker.subscribe(events.PREFERENCES_CHANGED, self._on_preferences_changed)

    def _on_state_changed(self, emitting_widget, enabled):
        is_active = self.get_active()
        Preferences.set(self._preference_key, is_active)

    def _on_preferences_changed(self, preference_key, value):
        if preference_key == self._preference_key:
            self.set_active(value)
