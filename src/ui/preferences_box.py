from gi.repository import Gtk

from ..monitor_type import MonitorType
from .monitor_enable_switch import MonitorEnableSwitch
from .theme_toggle_manager import ThemeToggleManager


@Gtk.Template(resource_path='/org/github/jorchube/monitorets/gtk/preferences-box.ui')
class PreferencesBox(Gtk.Box):
    __gtype_name__ = 'PreferencesBox'

    _cpu_monitor_enable_action_row = Gtk.Template.Child()
    _gpu_monitor_enable_action_row = Gtk.Template.Child()
    _memory_monitor_enable_action_row = Gtk.Template.Child()

    _system_theme_toggle_button = Gtk.Template.Child()
    _light_theme_toggle_button = Gtk.Template.Child()
    _dark_theme_toggle_button = Gtk.Template.Child()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._theme_toggle_wrapper = ThemeToggleManager(self)

        self._setup_monitor_enable_action_row(MonitorType.CPU, "cpu_monitor.enabled", self._cpu_monitor_enable_action_row)
        self._setup_monitor_enable_action_row(MonitorType.GPU, "gpu_monitor.enabled", self._gpu_monitor_enable_action_row)
        self._setup_monitor_enable_action_row(MonitorType.Memory, "memory_monitor.enabled", self._memory_monitor_enable_action_row)

    def _setup_monitor_enable_action_row(self, monitor_type, enabled_preference_key, action_row):
        switch = MonitorEnableSwitch(monitor_type, enabled_preference_key)
        self._add_switch_to_action_row(switch, action_row)

    def _add_switch_to_action_row(self, switch, action_row):
        action_row.add_suffix(switch)
        action_row.set_activatable_widget(switch)
