from .monitor_widget import MonitorWidget
from ...monitors.memory_monitor import MemoryMonitor
from .. import colors


class MemoryMonitorWidget(MonitorWidget):
    def __init__(self, *args, **kwargs):
        self._title = "Memory"
        self._color = colors.ORANGE
        self._monitor = MemoryMonitor()

        super().__init__(self._monitor, self._title, self._color, *args, **kwargs)
