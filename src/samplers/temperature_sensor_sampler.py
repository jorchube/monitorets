import psutil

from .sampler import Sampler
from .sample import Sample


class TemperatureSensorSampler(Sampler):
    _MAX_CELSIUS = 100
    _MAX_FAHRENHEIT = 212

    def __init__(self, temperature_sensor_descriptor, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._sensor_descriptor = temperature_sensor_descriptor
        self._fahrenheit = False

    def set_celsius(self):
        self._fahrenheit = False

    def set_fahrenheit(self):
        self._fahrenheit = True

    def _get_sample(self):
        discovered_hardware = psutil.sensors_temperatures()
        sensor_list = discovered_hardware[self._sensor_descriptor.hardware_name]

        for sensor in sensor_list:
            if sensor.label == self._sensor_descriptor.hardware_sensor_name:
                sample = self._get_sample_from_sensor(sensor)
                return sample

        return Sample(to_plot=0, single_value=0, units="-")

    def _get_sample_from_sensor(self, sensor):
        max_default = self._MAX_CELSIUS
        units = self._get_units()

        current_temp = sensor.current
        max_temp = sensor.high if sensor.high else max_default
        temp_as_percent = self._get_temp_as_percent(current_temp, max_temp)

        single_value = current_temp
        if self._fahrenheit:
            single_value = self._celsius_to_fahrenheit(current_temp)

        sample = Sample(
            to_plot=int(temp_as_percent), single_value=round(single_value), units=units
        )

        return sample

    def _get_units(self):
        return "℉" if self._fahrenheit else "℃"

    def _get_temp_as_percent(self, current_temp, max_temp):
        return (current_temp * 100) / max_temp

    def _celsius_to_fahrenheit(self, celsius):
        return (celsius * 1.8) + 32
