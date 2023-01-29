from .monitor import Monitor
from ..samplers.temperature_sensor_sampler import TemperatureSensorSampler
from ..event_broker import EventBroker
from .. import events
from ..preference_keys import PreferenceKeys
from ..temperature import FAHRENHEIT
from ..preferences import Preferences


class TemperatureMonitor(Monitor):
    def __init__(self, temperature_sensor_descriptor):
        sampler = TemperatureSensorSampler(temperature_sensor_descriptor)
        super().__init__(sampler)

        temperature_units = Preferences.get(PreferenceKeys.TEMPERATURE_UNITS)
        self._set_temperature_units(temperature_units)
        EventBroker.subscribe(events.PREFERENCES_CHANGED, self._on_preference_changed)

    def _on_preference_changed(self, preference_key, value):
        if preference_key == PreferenceKeys.TEMPERATURE_UNITS:
            self._set_temperature_units(value)

    def _set_temperature_units(self, units):
        if units == FAHRENHEIT:
            self._sampler.set_fahrenheit()
        else:
            self._sampler.set_celsius()
