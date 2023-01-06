from .monitor_widget import MonitorWidget
from ...monitors.gpu_monitor import GpuMonitor
from .. import colors
from ...translatable_strings import monitor_title
from ...monitor_type import MonitorType


class GpuMonitorWidget(MonitorWidget):
    def __init__(self, *args, **kwargs):
        self._type = MonitorType.GPU
        self._title = monitor_title.GPU
        self._color = colors.GREEN
        self._monitor = GpuMonitor()

        super().__init__(self._monitor, self._type, self._title, self._color, *args, **kwargs)
