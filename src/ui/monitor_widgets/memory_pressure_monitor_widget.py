from .monitor_widget import MonitorWidget
from ...monitors.memory_pressure_monitor import MemoryPressureMonitor
from .. import colors
from ...translatable_strings import monitor_title
from ...monitor_type import MonitorType


class MemoryPressureMonitorWidget(MonitorWidget):
    def __init__(self, *args, **kwargs):
        self._type = MonitorType.MEMORY_PRESSURE
        self._title = monitor_title.MEMORY_PRESSURE
        self._color = colors.ORANGE
        self._monitor = MemoryPressureMonitor()

        super().__init__(
            self._monitor, self._type, self._title, self._color, *args, **kwargs
        )
