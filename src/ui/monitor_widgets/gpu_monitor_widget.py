from .monitor_widget import MonitorWidget
from ...monitors.gpu_monitor import GpuMonitor
from ..graph_area import GraphArea
from .. import colors


class GpuMonitorWidget(MonitorWidget):
    def __init__(self, *args, **kwargs):
        self._title = "GPU"
        self._color = colors.GREEN
        self._monitor = GpuMonitor()

        super().__init__(self._monitor, self._title, self._color, *args, **kwargs)
