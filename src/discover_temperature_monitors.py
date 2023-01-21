import psutil

from .temperature_sensors.temperature_sensor_descriptor import (
    TemperatureSensorDescriptor,
)
from .ui.monitor_widgets.temperature_sensor_monitor_widget import (
    TemperatureSensorMonitorWidget,
)
from .monitor_descriptors import register_monitor_descriptor
from .preferences import Preferences
from .translatable_strings import (
    preference_toggle_label,
    preference_toggle_section_name,
)


def _get_sensor_descriptors():
    sensors = psutil.sensors_temperatures()
    if not sensors:
        return list()

    sensor_descriptor_list = list()
    for hardware_name, hardware_sensor_list in sensors.items():
        for hardware_sensor in hardware_sensor_list:
            hardware_sensor_name = hardware_sensor.label
            descriptor = TemperatureSensorDescriptor(
                hardware_name, hardware_sensor_name
            )
            sensor_descriptor_list.append(descriptor)

    return sensor_descriptor_list


def _build_monitor_descriptor(sensor_descriptor):
    sensor_id = (
        f"{sensor_descriptor.hardware_name}-{sensor_descriptor.hardware_sensor_name}"
    )
    monitor_type = f"temperature_sensor_{sensor_id}"
    enabled_preference_key = f"temp_monitor.{sensor_id}.enabled"
    widget_constructor = lambda: TemperatureSensorMonitorWidget(
        monitor_type, sensor_descriptor
    )
    _preference_toggle_label = f"{sensor_id}"
    _preference_toggle_section_name = preference_toggle_section_name.TEMPERATURE

    return {
        "type": monitor_type,
        "enabled_preference_key": enabled_preference_key,
        "monitor_class": widget_constructor,
        "preference_toggle_label": _preference_toggle_label,
        "preference_toggle_description": None,
        "preference_toggle_section_name": _preference_toggle_section_name,
    }


def execute():
    sensor_descriptor_list = _get_sensor_descriptors()

    for sensor_descriptor in sensor_descriptor_list:
        monitor_descriptor = _build_monitor_descriptor(sensor_descriptor)
        register_monitor_descriptor(monitor_descriptor)
        Preferences.register_preference_key_default(
            monitor_descriptor["enabled_preference_key"], False
        )
