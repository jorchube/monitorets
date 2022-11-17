from .monitor_widget import MonitorWidget
from ...monitors.temperature_monitor import TemperatureMonitor
from .. import colors

class TemperatureSensorMonitorWidget(MonitorWidget):
    def __init__(self, temperature_sensor_descriptor, *args, **kwargs):
        name = f"{temperature_sensor_descriptor.hardware_name}-{temperature_sensor_descriptor.hardware_sensor_name}"
        self._title = f"Temp ({name})"
        self._color = colors.RED
        self._monitor = TemperatureMonitor(temperature_sensor_descriptor)

        import pprint
        pprint.pp(self)

        super().__init__(self._monitor, self._title, self._color, *args, **kwargs)
