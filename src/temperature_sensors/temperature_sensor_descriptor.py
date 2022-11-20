from dataclasses import dataclass


@dataclass
class TemperatureSensorDescriptor:
    hardware_name: str
    hardware_sensor_name: str
