from gi.repository import Adw
from gi.repository import GLib
from gi.repository import Gtk
from gi.repository import GObject

from .monitor_enable_row import MonitorEnableRow


@Gtk.Template(resource_path='/org/github/jorchube/gpumonitor/gtk/preferences-box.ui')
class PreferencesBox(Gtk.Box):
    __gtype_name__ = 'PreferencesBox'

    _cpu_monitor_enable_action_row = Gtk.Template.Child()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._initialize_cpu_monitor_enable_action_row()

    def _initialize_cpu_monitor_enable_action_row(self):
        monitor_enable_switch = MonitorEnableSwitch()

        self._cpu_monitor_enable_action_row.add_suffix(monitor_enable_switch)
        self._cpu_monitor_enable_action_row.set_activatable_widget(monitor_enable_switch)


class MonitorEnableSwitch(Gtk.Switch):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_valign(Gtk.Align.CENTER)
        self.connect("state-set", self._on_state_changed)

    def _on_state_changed(self, emitting_widget, enabled):
        print(f"monitor enabled: {enabled}")
