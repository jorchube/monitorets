from gi.repository import Adw, Gtk
from ...preferences import Preferences
from ...preference_keys import PreferenceKeys
from ...translatable_strings import redraw_frequency as redraw_frequency_labels
from .. import monitor_redraw_frequency_seconds_values as redraw_frequency_values


class RedrawFrequencyToggleWidget(Adw.Bin):
    def __init__(self):
        super().__init__()
        self.set_margin_top(10)
        self.set_margin_bottom(10)

        self._options_map = {
            0: {
                "value": redraw_frequency_values.VERY_HIGH,
                "label": redraw_frequency_labels.VERY_HIGH
            },
            1: {
                "value": redraw_frequency_values.HIGH,
                "label": redraw_frequency_labels.HIGH
            },
            2: {
                "value": redraw_frequency_values.LOW,
                "label": redraw_frequency_labels.LOW
            },
            3: {
                "value": redraw_frequency_values.VERY_LOW,
                "label": redraw_frequency_labels.VERY_LOW
            },
        }

        combo_box = Gtk.DropDown.new_from_strings(self._get_dropdown_options())
        self.set_child(combo_box)
        self._mark_current_selected_item(combo_box)

        combo_box.connect("notify::selected", self._on_selected_item)

    def _mark_current_selected_item(self, combo_box):
        current_value = Preferences.get(PreferenceKeys.REDRAW_FREQUENCY_SECONDS)
        current_index = self._get_index_for_frequency(current_value)
        combo_box.set_selected(current_index)

    def _on_selected_item(self, dropdown, _):
        index = dropdown.get_selected()
        redraw_frequency = self._get_frequency_for_index(index)
        Preferences.set(PreferenceKeys.REDRAW_FREQUENCY_SECONDS, redraw_frequency)

    def _get_dropdown_options(self):
        return [
            self._options_map[0]["label"],
            self._options_map[1]["label"],
            self._options_map[2]["label"],
            self._options_map[3]["label"],
        ]

    def _get_frequency_for_index(self, index):
        return self._options_map[index]["value"]

    def _get_index_for_frequency(self, value):
        for index in range(len(self._options_map)):
            if self._options_map[index]["value"] == value:
                return index
