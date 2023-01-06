from .monitor_widget import MonitorWidget
from ...monitors.cpu_monitor import CpuMonitor
from .. import colors
from ...translatable_strings import monitor_title
from ...monitor_type import MonitorType


class CpuMonitorWidget(MonitorWidget):
    def __init__(self, *args, **kwargs):
        self._type = MonitorType.CPU
        self._title = monitor_title.CPU
        self._color = colors.BLUE
        self._monitor = CpuMonitor()

        super().__init__(self._monitor, self._type, self._title, self._color, *args, **kwargs)
