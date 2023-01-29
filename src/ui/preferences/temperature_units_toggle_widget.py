from gi.repository import Adw, Gtk
from ...preferences import Preferences
from ...preference_keys import PreferenceKeys
from ...temperature import CELSIUS, FAHRENHEIT


class TemperatureUnitsToggleWidget(Adw.Bin):
    def __init__(self):
        super().__init__()
        self.set_margin_top(10)
        self.set_margin_bottom(10)

        self._fahrenheit_toggle = Gtk.ToggleButton(label="℉")
        self._celsius_toggle = Gtk.ToggleButton(label="℃")
        self._celsius_toggle.set_group(self._fahrenheit_toggle)

        buttons_container = Gtk.Box(orientation= Gtk.Orientation.HORIZONTAL)
        buttons_container.add_css_class("linked")
        buttons_container.append(self._celsius_toggle)
        buttons_container.append(self._fahrenheit_toggle)
        self.set_child(buttons_container)

        self._set_current_active_toggle()
        self._celsius_toggle.connect("toggled", self._on_celsius_toggled)
        self._fahrenheit_toggle.connect("toggled", self._on_fahrenheit_toggled)

    def _set_current_active_toggle(self):
        current_units = Preferences.get(PreferenceKeys.TEMPERATURE_UNITS)
        self._celsius_toggle.set_active(current_units == CELSIUS)
        self._fahrenheit_toggle.set_active(current_units == FAHRENHEIT)

    def _on_celsius_toggled(self, *_):
        if self._celsius_toggle.get_active():
            Preferences.set(PreferenceKeys.TEMPERATURE_UNITS, CELSIUS)

    def _on_fahrenheit_toggled(self, *_):
        if self._fahrenheit_toggle.get_active():
            Preferences.set(PreferenceKeys.TEMPERATURE_UNITS, FAHRENHEIT)
