from .monitor import Monitor
from ..samplers.temperature_sensor_sampler import TemperatureSensorSampler


class TemperatureMonitor(Monitor):
    def __init__(self, temperature_sensor_descriptor):
        sampler = TemperatureSensorSampler(temperature_sensor_descriptor)
        super().__init__(sampler)
