from .monitor_widget import MonitorWidget
from ..relative_graph_area import RelativeGraphArea


class RelativeMonitorWidget(MonitorWidget):
    def _graph_area_instance(self, color, redraw_freq_seconds, draw_smooth_graph):
        return RelativeGraphArea(color, redraw_freq_seconds, draw_smooth_graph)
