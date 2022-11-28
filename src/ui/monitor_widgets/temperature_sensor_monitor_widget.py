from .gradient_monitor_widget import GradientMonitorWidget
from ...monitors.temperature_monitor import TemperatureMonitor
from .. import colors
from ...translatable_strings import monitor_title

class TemperatureSensorMonitorWidget(GradientMonitorWidget):
    def __init__(self, temperature_sensor_descriptor, *args, **kwargs):
        name = f"{temperature_sensor_descriptor.hardware_name}-{temperature_sensor_descriptor.hardware_sensor_name}"
        self._title = f"{monitor_title.TEMPERATURE} ({name})"
        self._title_color = colors.BROWN
        self._start_color = colors.GREEN
        self._end_color = colors.RED
        self._monitor = TemperatureMonitor(temperature_sensor_descriptor)

        super().__init__(self._monitor, self._title, self._title_color, self._start_color, self._end_color, *args, **kwargs)
