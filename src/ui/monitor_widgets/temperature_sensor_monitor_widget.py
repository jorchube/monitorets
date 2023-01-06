from .monitor_widget import MonitorWidget
from ...monitors.temperature_monitor import TemperatureMonitor
from .. import colors


class TemperatureSensorMonitorWidget(MonitorWidget):
    def __init__(self, monitor_type, temperature_sensor_descriptor, *args, **kwargs):
        name = f"{temperature_sensor_descriptor.hardware_name}-{temperature_sensor_descriptor.hardware_sensor_name}"
        self._type = monitor_type
        self._title = f"🌡{name}"
        self._color = colors.BROWN
        self._monitor = TemperatureMonitor(temperature_sensor_descriptor)

        super().__init__(self._monitor, self._type, self._title, self._color, *args, **kwargs)
