from .monitor_widget import MonitorWidget
from ...monitors.root_usage_monitor import RootUsageMonitor
from .. import colors
from ...translatable_strings import monitor_title
from ...monitor_type import MonitorType


class RootUsageMonitorWidget(MonitorWidget):
    def __init__(self, *args, **kwargs):
        self._type = MonitorType.Root_usage
        self._title = monitor_title.ROOT_USAGE
        self._color = colors.PURPLE
        self._monitor = RootUsageMonitor()

        super().__init__(
            self._monitor, self._type, self._title, self._color, *args, **kwargs
        )
