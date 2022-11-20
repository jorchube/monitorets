from .monitor_widget import MonitorWidget
from ..gradient_graph_area import GradientGraphArea


class GradientMonitorWidget(MonitorWidget):
    def __init__(self, monitor, title, title_color, start_color=None, end_color=None, redraw_freq_seconds=MonitorWidget._REDRAW_FREQUENCY_SECONDS, *args, **kwargs):
        self._start_color = start_color
        self._end_color = end_color
        super().__init__(monitor, title, title_color, redraw_freq_seconds, *args, **kwargs)

    def _graph_area_instance(self, color, redraw_freq_seconds):
        return GradientGraphArea(self._start_color, self._end_color, redraw_freq_seconds)
