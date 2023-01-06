from .overlapping_values_monitor_widget import OverlappingGraphsMonitorWidget
from ...monitors.cpu_per_core_monitor import CpuPerCoreMonitor
from .. import colors
from ...translatable_strings import monitor_title
from ...monitor_type import MonitorType


class CpuPerCoreMonitorWidget(OverlappingGraphsMonitorWidget):
    def __init__(self, *args, **kwargs):
        self._type = MonitorType.CPU_PER_CORE
        self._title = monitor_title.CPU
        self._color = colors.BLUE
        self._monitor = CpuPerCoreMonitor()

        super().__init__(self._monitor, self._type, self._title, self._color, *args, **kwargs)
