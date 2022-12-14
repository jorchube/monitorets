from .monitor_widget import MonitorWidget
from ..overlapping_graphs_area import OverlappingGraphsArea


class OverlappingGraphsMonitorWidget(MonitorWidget):
    def _graph_area_instance(self, color, redraw_freq_seconds, draw_smooth_graph):
        return OverlappingGraphsArea(color, redraw_freq_seconds, draw_smooth_graph)
