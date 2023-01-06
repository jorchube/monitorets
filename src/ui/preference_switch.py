from gi.repository import Gtk

from ..preferences import Preferences


class PreferenceSwitch(Gtk.Switch):
    def __init__(self, preference_key, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_valign(Gtk.Align.CENTER)
        self._preference_key = preference_key

        is_active = Preferences.get(self._preference_key)
        self.set_active(is_active)

        self.connect("state-set", self._on_state_changed)

    def _on_state_changed(self, emitting_widget, enabled):
        is_active = self.get_active()
        Preferences.set(self._preference_key, is_active)
