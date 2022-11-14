from .relative_monitor_widget import RelativeMonitorWidget
from ...monitors.uplink_monitor import UplinkMonitor
from .. import colors


class UplinkMonitorWidget(RelativeMonitorWidget):
    def __init__(self, *args, **kwargs):
        self._title = "Network 🠅"
        self._color = colors.RED
        self._monitor = UplinkMonitor()

        super().__init__(self._monitor, self._title, self._color, *args, **kwargs)
