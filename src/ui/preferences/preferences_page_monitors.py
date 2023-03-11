from gi.repository import Adw, Gtk

from ...translatable_strings import preference_toggle_section_name
from .monitor_preference_row import MonitorPreferenceRow
from ...monitor_descriptors import (
    get_monitor_descriptors_grouped_by_preference_toggle_section,
)


@Gtk.Template(
    resource_path="/org/github/jorchube/monitorets/gtk/preferences-page-monitors.ui"
)
class PreferencesPageMonitors(Adw.PreferencesPage):
    __gtype_name__ = "PreferencesPageMonitors"

    _cpu_preferences_group = Gtk.Template.Child()
    _gpu_preferences_group = Gtk.Template.Child()
    _memory_preferences_group = Gtk.Template.Child()
    _network_preferences_group = Gtk.Template.Child()
    _disk_preferences_group = Gtk.Template.Child()
    _pressure_preferences_group = Gtk.Template.Child()
    _temperature_preferences_group = Gtk.Template.Child()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._add_toggles()

    def _add_toggles(self):
        descriptors = get_monitor_descriptors_grouped_by_preference_toggle_section()

        for descriptor in descriptors[preference_toggle_section_name.CPU]:
            self._add_toggle_to_group(descriptor, self._cpu_preferences_group)

        for descriptor in descriptors[preference_toggle_section_name.GPU]:
            self._add_toggle_to_group(descriptor, self._gpu_preferences_group)

        for descriptor in descriptors[preference_toggle_section_name.MEMORY]:
            self._add_toggle_to_group(descriptor, self._memory_preferences_group)

        for descriptor in descriptors[preference_toggle_section_name.NETWORK]:
            self._add_toggle_to_group(descriptor, self._network_preferences_group)

        for descriptor in descriptors[preference_toggle_section_name.DISK_USAGE]:
            self._add_toggle_to_group(descriptor, self._disk_preferences_group)

        for descriptor in descriptors[preference_toggle_section_name.PRESSURE]:
            self._add_toggle_to_group(descriptor, self._pressure_preferences_group)

        for descriptor in descriptors[preference_toggle_section_name.TEMPERATURE]:
            self._add_toggle_to_group(descriptor, self._temperature_preferences_group)

    def _add_toggle_to_group(self, monitor_descriptor, group):
        action_row = self._build_toggle_action_row(monitor_descriptor)
        group.add(action_row)

    def _build_toggle_action_row(self, monitor_descriptor):
        monitor_type = monitor_descriptor["type"]
        label = monitor_descriptor["preference_toggle_label"]
        enabled_preference_key = monitor_descriptor["enabled_preference_key"]
        description = monitor_descriptor.get("preference_toggle_description")

        return MonitorPreferenceRow(
            monitor_type, label, enabled_preference_key, subtitle=description
        )
