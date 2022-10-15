from time import monotonic
from gi.repository import Adw, GLib, Gtk, GObject

from ..event_broker import EventBroker
from .. import events
from ..monitor_type import MonitorType


@Gtk.Template(resource_path='/org/github/jorchube/gpumonitor/gtk/preferences-box.ui')
class PreferencesBox(Gtk.Box):
    __gtype_name__ = 'PreferencesBox'

    _cpu_monitor_enable_action_row = Gtk.Template.Child()
    _gpu_monitor_enable_action_row = Gtk.Template.Child()
    _memory_monitor_enable_action_row = Gtk.Template.Child()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._initialize_monitor_enable_action_row(MonitorType.CPU, self._cpu_monitor_enable_action_row)
        self._initialize_monitor_enable_action_row(MonitorType.GPU, self._gpu_monitor_enable_action_row)
        self._initialize_monitor_enable_action_row(MonitorType.Memory, self._memory_monitor_enable_action_row)

    def _initialize_monitor_enable_action_row(self, monitor_type, action_row):
        monitor_enable_switch = MonitorEnableSwitch(monitor_type=monitor_type)
        action_row.add_suffix(monitor_enable_switch)
        action_row.set_activatable_widget(monitor_enable_switch)


class MonitorEnableSwitch(Gtk.Switch):

    def __init__(self, monitor_type,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_valign(Gtk.Align.CENTER)
        self._monitor_type = monitor_type
        self.connect("state-set", self._on_state_changed)

    def _on_state_changed(self, emitting_widget, enabled):
        EventBroker.notify(events.MONITOR_ENABLED_CHANGED, self._monitor_type, self.get_active())
