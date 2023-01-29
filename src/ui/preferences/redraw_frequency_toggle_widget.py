from gi.repository import Adw, Gtk
from ...preferences import Preferences
from ...preference_keys import PreferenceKeys
from ...translatable_strings import redraw_frequency


class RedrawFrequencyToggleWidget(Adw.Bin):
    def __init__(self):
        super().__init__()
        self.set_margin_top(10)
        self.set_margin_bottom(10)

        options = [
            redraw_frequency.VERY_HIGH,
            redraw_frequency.HIGH,
            redraw_frequency.LOW,
            redraw_frequency.VERY_LOW,
        ]
        self._frequency_by_position = [0.05, 0.1, 0.5, 1]

        combo_box = Gtk.DropDown.new_from_strings(options)
        self.set_child(combo_box)

        combo_box.connect("notify::selected", self._on_selected_item)

    def _on_selected_item(self, dropdown, _):
        print(f"{dropdown.get_selected()}")
