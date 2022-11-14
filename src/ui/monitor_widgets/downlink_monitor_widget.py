from .relative_monitor_widget import RelativeMonitorWidget
from ...monitors.downlink_monitor import DownlinkMonitor
from .. import colors


class DownlinkMonitorWidget(RelativeMonitorWidget):
    def __init__(self, *args, **kwargs):
        self._title = "Network 🠇"
        self._color = colors.BLUE
        self._monitor = DownlinkMonitor()

        super().__init__(self._monitor, self._title, self._color, *args, **kwargs)
