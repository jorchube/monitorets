import math
import cairo
from gi.repository import Gtk, GObject
from .graph_area import GraphArea


class OverlappingGraphsArea(GraphArea):
    def __init__(self, color, redraw_frequency_seconds):
        super().__init__(color, redraw_frequency_seconds)
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

    def _draw_values_fill(self, context, values, width, height):
        context.new_path()
        context.set_line_join(cairo.LINE_JOIN_ROUND)
        context.set_line_cap(cairo.LINE_CAP_ROUND)

        self._draw_values_shape(context, values, width, height, close=True)

        context.set_source_rgba(*self._color, self._ALPHA_FILL)
        context.fill()

    def _draw_values_ouline(self, context, values, width, height):
        context.new_path()
        context.set_line_join(cairo.LINE_JOIN_ROUND)
        context.set_line_cap(cairo.LINE_CAP_ROUND)

        self._draw_values_shape(context, values, width, height)

        context.set_line_width(self._LINE_WIDTH)
        context.set_source_rgba(*self._color, 1)
        context.stroke()

    def _draw_values_shape(self, context, values, width, height, close=False):
        order = 0

        for value in values:
            x, y = self._value_point(width, height, value, order)
            context.line_to(x, y)
            order += 1

        if close:
            context.line_to(x, height)
            context.line_to(width, height)
            context.close_path()
