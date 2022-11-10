from .monitor_widget import MonitorWidget
from ...monitors.home_usage_monitor import HomeUsageMonitor
from .. import colors


class HomeUsageMonitorWidget(MonitorWidget):
    def __init__(self, *args, **kwargs):
        self._title = "~"
        self._color = colors.PURPLE
        self._monitor = HomeUsageMonitor()

        super().__init__(self._monitor, self._title, self._color, *args, **kwargs)
