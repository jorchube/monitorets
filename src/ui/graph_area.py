import math
import cairo
from gi.repository import Gtk, GObject


class GraphArea:
    _LINE_WIDTH = 0.2
    _ALPHA_FILL = 0.2
    _MASK_CORNER_RADIUS = 12
    _DEFAULT_WIDTH_PER_SAMPLE = 10

    def __init__(self, color, redraw_frequency_seconds, smooth_graph=False):
        self._color = color.RGB
        self._redraw_frequency_seconds = redraw_frequency_seconds
        self._width_per_sample = None
        self.set_width_per_sample(self._DEFAULT_WIDTH_PER_SAMPLE)
        self._drawing_area = self._build_drawing_area()
        self._drawing_area.set_draw_func(self._draw_func, None)
        self._values = None
        self._current_x_step_offset = 0
        self._draw_smooth_graph = smooth_graph

    def set_width_per_sample(self, value):
        self._width_per_sample = value
        self._x_step_per_tick = self._width_per_sample * self._redraw_frequency_seconds

    def set_new_values(self, values):
        self._values = values
        self._current_x_step_offset = self._width_per_sample

    def get_drawing_area_widget(self):
        return self._drawing_area

    def redraw_tick(self):
        GObject.idle_add(self._redraw)
        self._current_x_step_offset -= self._x_step_per_tick

    def _build_drawing_area(self):
        drawing_area = Gtk.DrawingArea()
        drawing_area.set_hexpand(True)
        drawing_area.set_vexpand(True)

        return drawing_area

    def _redraw(self):
        self._drawing_area.queue_draw()

    def _draw_func(self, gtk_drawing_area, context, width, height, user_data):
        if self._values is None:
            return
        values = self._values

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
        if self._draw_smooth_graph is True:
            self._smooth_draw_values_shape(context, values, width, height, close)
        else:
            self._fast_draw_values_shape(context, values, width, height, close)

    def _fast_draw_values_shape(self, context, values, width, height, close=False):
        order = 0

        for value in values:
            x, y = self._value_point(width, height, value, order)
            context.line_to(x, y)
            order += 1

        if close:
            context.line_to(x, height)
            context.line_to(width, height)
            context.close_path()

    def _value_point(self, width, height, value, order):
        x = width - (order * self._width_per_sample) + self._current_x_step_offset
        y = height - (height * (value / 100.0))

        return x, y

    def _smooth_draw_values_shape(self, context, values, width, height, close=False):
        order = 0

        x, _ = self._smooth_value_point(width, height, values[0], order)

        for i in range(len(values) - 1):
            v0 = values[i]
            v3 = values[i + 1]

            x0, y0 = self._smooth_value_point(width, height, v0, order)
            x3, y3 = self._smooth_value_point(width, height, v3, order + 1)

            mid_x = (x0 + x3) / 2
            x1, y1 = mid_x, y0
            x2, y2 = mid_x, y3

            context.curve_to(x1, y1, x2, y2, x3, y3)
            order += 1
            x = x3

        if close:
            context.line_to(x, height)
            context.line_to(width, height)
            context.close_path()

    def _smooth_value_point(self, width, height, value, order):
        x = width - ((order - 1) * self._width_per_sample) + self._current_x_step_offset
        y = height - (height * (value / 100.0))

        return x, y

    def _apply_mask(self, context, width, height):
        context.set_operator(cairo.OPERATOR_DEST_IN)
        context.new_path()
        self._rectangle_path_with_corner_radius(
            context, width, height, self._MASK_CORNER_RADIUS
        )
        context.close_path()
        context.fill()

    def _rectangle_path_with_corner_radius(self, context, width, height, radius):
        context.new_path()

        context.line_to(width, height - radius)
        context.arc(width - radius, height - radius, radius, 0, math.pi / 2)
        context.line_to(radius, height)
        context.arc(radius, height - radius, radius, math.pi / 2, math.pi)
        context.line_to(0, radius)
        context.arc(radius, radius, radius, math.pi, (3 / 2) * math.pi)
        context.line_to(width - radius, 0)
        context.arc(width - radius, radius, radius, (3 / 2) * math.pi, 0)
