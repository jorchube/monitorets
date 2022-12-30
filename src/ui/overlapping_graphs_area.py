from .graph_area import GraphArea


class OverlappingGraphsArea(GraphArea):
    def __init__(self, color, redraw_frequency_seconds, draw_smooth_graph):
        super().__init__(color, redraw_frequency_seconds, smooth_graph=draw_smooth_graph)
        self._ALPHA_FILL = None

    def _draw_func(self, gtk_drawing_area, context, width, height, user_data):
        if self._values is None:
            return

        if self._ALPHA_FILL is None:
            self._ALPHA_FILL = (super()._ALPHA_FILL / len(self._values)) * 2.0

        values_lists = self._values

        for values in values_lists:
            self._draw_values_fill(context, values, width, height)
            self._draw_values_ouline(context, values, width, height)

        self._apply_mask(context, width, height)
