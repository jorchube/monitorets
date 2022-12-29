import math
import cairo
from gi.repository import Gtk, GObject
from .graph_area import GraphArea


class GradientGraphArea(GraphArea):
    def __init__(self, start_color, end_color, redraw_frequency_seconds):
        self._start_color = start_color.RGB
        self._end_color = end_color.RGB
        super().__init__(start_color, redraw_frequency_seconds)

    def _draw_values_fill(self, context, values, width, height):
        context.new_path()
        context.set_line_join(cairo.LINE_JOIN_ROUND)
        context.set_line_cap(cairo.LINE_CAP_ROUND)

        self._draw_values_shape(context, values, width, height, close=True)

        gradient = cairo.LinearGradient(0, 0, 0, height)
        gradient.add_color_stop_rgba(0, *self._end_color, self._ALPHA_FILL)
        gradient.add_color_stop_rgba(0.5, *self._start_color, self._ALPHA_FILL)
        gradient.add_color_stop_rgba(1, *self._start_color, self._ALPHA_FILL)
        context.set_source(gradient)

        context.fill()

    def _draw_values_ouline(self, context, values, width, height):
        context.new_path()
        context.set_line_join(cairo.LINE_JOIN_ROUND)
        context.set_line_cap(cairo.LINE_CAP_ROUND)

        self._draw_values_shape(context, values, width, height)

        context.set_line_width(self._LINE_WIDTH)

        gradient = cairo.LinearGradient(0, 0, 0, height)
        gradient.add_color_stop_rgba(0, *self._end_color, 1)
        gradient.add_color_stop_rgba(0.5, *self._start_color, 1)
        gradient.add_color_stop_rgba(1, *self._start_color, 1)
        context.set_source(gradient)

        context.stroke()
