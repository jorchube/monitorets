from .monitor_widget import MonitorWidget
from ...monitors.cpu_monitor import CpuMonitor
from .. import colors
from ...translatable_strings import monitor_title


class CpuMonitorWidget(MonitorWidget):
    def __init__(self, *args, **kwargs):
        self._title = monitor_title.CPU
        self._color = colors.BLUE
        self._monitor = CpuMonitor()

        super().__init__(self._monitor, self._title, self._color, *args, **kwargs)
