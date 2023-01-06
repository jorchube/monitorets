from .relative_monitor_widget import RelativeMonitorWidget
from ...monitors.uplink_monitor import UplinkMonitor
from .. import colors
from ...translatable_strings import monitor_title
from ...monitor_type import MonitorType


class UplinkMonitorWidget(RelativeMonitorWidget):
    def __init__(self, *args, **kwargs):
        self._type = MonitorType.Uplink
        self._title = monitor_title.UPLINK
        self._color = colors.RED
        self._monitor = UplinkMonitor()

        super().__init__(self._monitor, self._type, self._title, self._color, *args, **kwargs)
