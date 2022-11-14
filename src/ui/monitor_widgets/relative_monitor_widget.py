from .monitor_widget import MonitorWidget
from ..relative_graph_area import RelativeGraphArea


class RelativeMonitorWidget(MonitorWidget):
    def __init__(self, monitor, title, color=None, redraw_freq_seconds=MonitorWidget._REDRAW_FREQUENCY_SECONDS, *args, **kwargs):
        super().__init__(monitor, title, color, redraw_freq_seconds, *args, **kwargs)

    def _graph_area_instance(self, color, redraw_freq_seconds):
        return RelativeGraphArea(color, redraw_freq_seconds)
