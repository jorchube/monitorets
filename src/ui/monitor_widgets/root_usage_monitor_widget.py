from .monitor_widget import MonitorWidget
from ...monitors.root_usage_monitor import RootUsageMonitor
from .. import colors


class RootUsageMonitorWidget(MonitorWidget):
    def __init__(self, *args, **kwargs):
        self._title = "/"
        self._color = colors.PURPLE
        self._monitor = RootUsageMonitor()

        super().__init__(self._monitor, self._title, self._color, *args, **kwargs)
