import cairo




class GraphArea:
    _LINE_WIDTH = 1
    _ALPHA_FILL = 0.2
    _BUFFER_BEFORE_RELEASE_SAMPLE = 50
    _SPACING_PER_SECOND = 10

    def __init__(self, gtk_drawing_area, color=None, sampling_frequency_seconds=1.0):
        self._color = color.RGB
        self._gtk_drawing_area = gtk_drawing_area
        self._gtk_drawing_area.set_draw_func(self._draw_func, None)
        self._spacing = self._SPACING_PER_SECOND * sampling_frequency_seconds

        self._values = []

    def _redraw(self):
        self._gtk_drawing_area.queue_draw()

    def _draw_func(self, gtk_drawing_area, context, width, height, user_data):
        if not self._values:
            return

        self._release_samples_if_needed(width)

        self._plot_y_fill(context, width, height)
        self._plot_y_values(context, width, height)

    def _release_samples_if_needed(self, width):
        max_values = self._get_number_of_visible_values(width)
        if len(self._values) > max_values:
            self._values = self._values[:max_values]


    def add_value(self, value):
        self._values.insert(0, value)
        self._redraw()

    def _get_number_of_visible_values(self, width):
        return int(width / self._spacing) + self._BUFFER_BEFORE_RELEASE_SAMPLE

    def _plot_y_values(self, context, width, height):
        context.new_path()
        context.set_line_join(cairo.LINE_JOIN_ROUND)
        context.set_line_cap(cairo.LINE_CAP_ROUND)

        self._plot_data_points(context, width, height)

        context.set_line_width(self._LINE_WIDTH)
        context.set_source_rgba(*self._color, 1)
        context.stroke()

    def _plot_y_fill(self, context, width, height):
        context.new_path()
        context.set_line_join(cairo.LINE_JOIN_ROUND)
        context.set_line_cap(cairo.LINE_CAP_ROUND)

        self._plot_data_points(context, width, height, close=True)

        context.set_source_rgba(*self._color, self._ALPHA_FILL)
        context.fill()

    def _plot_data_points(self, context, width, height, close=False):
        points_drawn = 0

        for value in self._values:
            x = width - (points_drawn * (self._spacing))
            y = height - (height * (value/100.0))
            context.line_to(x, y)

            points_drawn = points_drawn + 1

        if close:
            context.line_to(x, height)
            context.line_to(width, height)
            context.close_path()
