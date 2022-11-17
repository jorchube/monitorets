from gi.repository import Gtk, Adw

from .monitor_enable_switch import MonitorEnableSwitch
from .theme_toggle_manager import ThemeToggleManager
from .layout_toggle_manager import LayoutToggleManager
from ..event_broker import EventBroker
from .. import events
from ..monitor_descriptors import get_monitor_descriptors_grouped_by_preference_toggle_section


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

        self._add_monitor_preference_toggles()

        self._about_button.connect("clicked", self._on_about_button_clicked)
        self._tips_button.connect("clicked", self._on_tips_button_clicked)

    def _add_monitor_preference_toggle(self, monitor_descriptor):
        if monitor_descriptor["preference_toggle_section_name"] is None:
            self._add_toplevel_monitor_enable_action_row_BIS(
                monitor_descriptor["preference_toggle_label"], monitor_descriptor["type"], monitor_descriptor["enabled_preference_key"]
            )

    def _add_monitor_preference_toggles(self):
        monitor_descriptors = get_monitor_descriptors_grouped_by_preference_toggle_section()

        for toplevel_descriptor in monitor_descriptors["toplevel"]:
            self._add_toplevel_monitor_enable_action_row(toplevel_descriptor)

        for section_name, descriptor_list in monitor_descriptors["section"].items():
            self._add_section_monitor_enable_action_rows(section_name, descriptor_list)

    def _add_toplevel_monitor_enable_action_row(self, monitor_descriptor):
        action_row = self._build_toggle_action_row(monitor_descriptor)
        self._monitor_enable_preferences_group.add(action_row)

    def _add_section_monitor_enable_action_rows(self, section_name, monitor_descriptor_list):
        expander_row = Adw.ExpanderRow()
        expander_row.set_title(section_name)

        for descriptor in monitor_descriptor_list:
            action_row = self._build_toggle_action_row(descriptor)
            expander_row.add_row(action_row)

        self._monitor_enable_preferences_group.add(expander_row)

    def _build_toggle_action_row(self, monitor_descriptor):
        label = monitor_descriptor["preference_toggle_label"]
        monitor_type = monitor_descriptor["type"]
        enabled_preference_key = monitor_descriptor["enabled_preference_key"]

        action_row = self._new_action_row()
        action_row.set_title(label)
        self._setup_monitor_enable_action_row(monitor_type, enabled_preference_key, action_row)

        return action_row

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
