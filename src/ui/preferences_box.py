from time import monotonic
from gi.repository import Adw, GLib, Gtk, GObject

from ..event_broker import EventBroker
from .. import events
from ..monitor_type import MonitorType
from ..preferences import Preferences


@Gtk.Template(resource_path='/org/github/jorchube/gpumonitor/gtk/preferences-box.ui')
class PreferencesBox(Gtk.Box):
    __gtype_name__ = 'PreferencesBox'

    _cpu_monitor_enable_action_row = Gtk.Template.Child()
    _gpu_monitor_enable_action_row = Gtk.Template.Child()
    _memory_monitor_enable_action_row = Gtk.Template.Child()

    def __init__(self, type, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type = type

        self._setup_monitor_enable_action_row(MonitorType.CPU, "cpu_monitor.enabled", self._cpu_monitor_enable_action_row)
        self._setup_monitor_enable_action_row(MonitorType.GPU, "gpu_monitor.enabled", self._gpu_monitor_enable_action_row)
        self._setup_monitor_enable_action_row(MonitorType.Memory, "memory_monitor.enabled", self._memory_monitor_enable_action_row)

    def _setup_monitor_enable_action_row(self, monitor_type, enabled_preference_key, action_row):
        switch = _MonitorEnableSwitch(monitor_type, enabled_preference_key)
        is_sensitive = monitor_type != self._type
        self._setup_action_row(monitor_type, switch, is_sensitive, action_row)

    def _setup_action_row(self, type, switch, is_sensitive, action_row):
        self._add_switch_to_action_row(switch, action_row)
        action_row.set_sensitive(is_sensitive)

    def _add_switch_to_action_row(self, switch, action_row):
        action_row.add_suffix(switch)
        action_row.set_activatable_widget(switch)

class _MonitorEnableSwitch(Gtk.Switch):
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
        EventBroker.notify(events.PREFERENCES_CHANGE_REQUESTED, self._preference_key, is_active)
        EventBroker.notify(events.MONITOR_ENABLED_CHANGED, self._monitor_type, is_active)

    def _on_preferences_changed(self, preference_key, value):
        if preference_key == self._preference_key:
            self.set_active(value)
