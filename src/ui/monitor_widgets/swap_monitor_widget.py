from .monitor_widget import MonitorWidget
from ...monitors.swap_monitor import SwapMonitor
from .. import colors
from ...translatable_strings import monitor_title


class SwapMonitorWidget(MonitorWidget):
    def __init__(self, *args, **kwargs):
        self._title = monitor_title.SWAP
        self._color = colors.PURPLE
        self._monitor = SwapMonitor()

        super().__init__(self._monitor, self._title, self._color, *args, **kwargs)
