from .monitor_widget import MonitorWidget
from ...monitors.io_pressure_monitor import IOPressureMonitor
from .. import colors
from ...translatable_strings import monitor_title
from ...monitor_type import MonitorType


class IOPressureMonitorWidget(MonitorWidget):
    def __init__(self, *args, **kwargs):
        self._type = MonitorType.IO_PRESSURE
        self._title = monitor_title.IO_PRESSURE
        self._color = colors.YELLOW
        self._monitor = IOPressureMonitor()

        super().__init__(
            self._monitor, self._type, self._title, self._color, *args, **kwargs
        )
