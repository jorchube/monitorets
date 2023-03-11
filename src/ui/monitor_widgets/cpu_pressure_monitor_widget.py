from .monitor_widget import MonitorWidget
from ...monitors.cpu_pressure_monitor import CpuPressureMonitor
from .. import colors
from ...translatable_strings import monitor_title
from ...monitor_type import MonitorType


class CpuPressureMonitorWidget(MonitorWidget):
    def __init__(self, *args, **kwargs):
        self._type = MonitorType.CPU_PRESSURE
        self._title = monitor_title.CPU_PRESSURE
        self._color = colors.BLUE
        self._monitor = CpuPressureMonitor()

        super().__init__(
            self._monitor, self._type, self._title, self._color, *args, **kwargs
        )
