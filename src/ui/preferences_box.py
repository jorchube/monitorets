from gi.repository import Gtk, Adw

from .monitor_enable_switch import MonitorEnableSwitch
from .theme_toggle_manager import ThemeToggleManager
from .layout_toggle_manager import LayoutToggleManager
from ..event_broker import EventBroker
from .. import events
from ..monitor_descriptors import monitor_descriptor_list


@Gtk.Template(resource_path='/org/github/jorchube/monitorets/gtk/preferences-box.ui')
class PreferencesBox(Gtk.Box):
    __gtype_name__ = 'PreferencesBox'

    _monitor_enable_preferences_group = Gtk.Template.Child()

    _system_theme_toggle_button = Gtk.Template.Child()
    _light_theme_toggle_button = Gtk.Template.Child()
    _dark_theme_toggle_button = Gtk.Template.Child()

    _adaptive_layout_toggle_button = Gtk.Template.Child()
    _horizontal_layout_toggle_button = Gtk.Template.Child()
    _vertical_layout_toggle_button = Gtk.Template.Child()

    _about_button = Gtk.Template.Child()
    _tips_button = Gtk.Template.Child()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._theme_toggle_manager = ThemeToggleManager(self)
        self._layout_toggle_manager = LayoutToggleManager(self)

        for descriptor in monitor_descriptor_list:
            self._add_monitor_enable_action_row(
                descriptor["preference_toggle_label"], descriptor["type"], descriptor["enabled_preference_key"]
            )

        self._about_button.connect("clicked", self._on_about_button_clicked)
        self._tips_button.connect("clicked", self._on_tips_button_clicked)

    def _add_monitor_enable_action_row(self, label, monitor_type, monitor_enabled_preference_key):
        action_row = self._new_action_row()
        action_row.set_title(label)
        self._setup_monitor_enable_action_row(monitor_type, monitor_enabled_preference_key, action_row)
        self._monitor_enable_preferences_group.add(action_row)

    def _setup_monitor_enable_action_row(self, monitor_type, enabled_preference_key, action_row):
        switch = MonitorEnableSwitch(monitor_type, enabled_preference_key)
        self._add_switch_to_action_row(switch, action_row)

    def _add_switch_to_action_row(self, switch, action_row):
        action_row.add_suffix(switch)
        action_row.set_activatable_widget(switch)

    def _on_about_button_clicked(self, user_data):
        EventBroker.notify(events.ABOUT_DIALOG_TRIGGERED)

    def _on_tips_button_clicked(self, user_data):
        EventBroker.notify(events.TIPS_DIALOG_TRIGGERED)

    def _new_action_row(self):
        return Adw.ActionRow()
