from .monitor_widget import MonitorWidget
from ...monitors.home_usage_monitor import HomeUsageMonitor
from .. import colors
from ...translatable_strings import monitor_title
from ...monitor_type import MonitorType


class HomeUsageMonitorWidget(MonitorWidget):
    def __init__(self, *args, **kwargs):
        self._type = MonitorType.Home_usage
        self._title = monitor_title.HOME_USAGE
        self._color = colors.PURPLE
        self._monitor = HomeUsageMonitor()

        super().__init__(self._monitor, self._type, self._title, self._color, *args, **kwargs)
