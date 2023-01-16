from .monitor_widget import MonitorWidget
from ...monitors.uplink_monitor import UplinkMonitor
from ..relative_graph_area import RelativeGraphArea
from .. import colors
from ...translatable_strings import monitor_title
from ...monitor_type import MonitorType


class UplinkMonitorWidget(MonitorWidget):
    def __init__(self, *args, **kwargs):
        self._type = MonitorType.Uplink
        self._title = monitor_title.UPLINK
        self._color = colors.RED
        self._monitor = UplinkMonitor()

        super().__init__(self._monitor, self._type, self._title, self._color, *args, **kwargs)

    def _graph_area_instance(self, color, redraw_freq_seconds, draw_smooth_graph):
        return RelativeGraphArea(color, redraw_freq_seconds, draw_smooth_graph)
