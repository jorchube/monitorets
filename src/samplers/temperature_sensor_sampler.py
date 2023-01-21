import psutil

from .sampler import Sampler
from .sample import Sample


class TemperatureSensorSampler(Sampler):
    def __init__(self, temperature_sensor_descriptor, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._sensor_descriptor = temperature_sensor_descriptor

    def _get_sample(self):
        discovered_hardware = psutil.sensors_temperatures()
        sensor_list = discovered_hardware[self._sensor_descriptor.hardware_name]

        for sensor in sensor_list:
            if sensor.label == self._sensor_descriptor.hardware_sensor_name:
                sample = self._get_sample_from_sensor(sensor)
                return sample

        return Sample(to_plot=0, single_value=0, units="-")

    def _get_sample_from_sensor(self, sensor):
        current_temp = sensor.current
        max_temp = sensor.high if sensor.high else 100

        temp_as_percent = (current_temp * 100) / max_temp

        sample = Sample(
            to_plot=int(temp_as_percent), single_value=round(current_temp), units="℃"
        )

        return sample
