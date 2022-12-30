from .monitor_widget import MonitorWidget
from ...monitors.temperature_monitor import TemperatureMonitor
from .. import colors
from ...translatable_strings import monitor_title


class TemperatureSensorMonitorWidget(MonitorWidget):
    def __init__(self, temperature_sensor_descriptor, *args, **kwargs):
        name = f"{temperature_sensor_descriptor.hardware_name}-{temperature_sensor_descriptor.hardware_sensor_name}"
        self._title = f"🌡{name}"
        self._color = colors.BROWN
        self._monitor = TemperatureMonitor(temperature_sensor_descriptor)

        super().__init__(self._monitor, self._title, self._color, *args, **kwargs)
