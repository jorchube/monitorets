from .monitor_widget import MonitorWidget
from ...monitors.memory_monitor import MemoryMonitor
from .. import colors
from ...translatable_strings import monitor_title
from ...monitor_type import MonitorType


class MemoryMonitorWidget(MonitorWidget):
    def __init__(self, *args, **kwargs):
        self._type = MonitorType.Memory
        self._title = monitor_title.MEMORY
        self._color = colors.ORANGE
        self._monitor = MemoryMonitor()

        super().__init__(self._monitor, self._type, self._title, self._color, *args, **kwargs)
