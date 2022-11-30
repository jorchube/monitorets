from .relative_monitor_widget import RelativeMonitorWidget
from ...monitors.downlink_monitor import DownlinkMonitor
from .. import colors
from ...translatable_strings import monitor_title


class DownlinkMonitorWidget(RelativeMonitorWidget):
    def __init__(self, *args, **kwargs):
        self._title = monitor_title.DOWNLINK
        self._color = colors.BLUE
        self._monitor = DownlinkMonitor()

        super().__init__(self._monitor, self._title, self._color, *args, **kwargs)
