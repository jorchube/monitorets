from .graph_area import GraphArea


class RelativeGraphArea(GraphArea):
    def __init__(self, color, redraw_frequency_seconds, draw_smooth_graph, new_reference_value_callback):
        self._minimum_reference_value = 1000
        self._reference_value = self._minimum_reference_value
        self._own_reference_value = self._minimum_reference_value
        self._new_reference_value_callback = new_reference_value_callback
        super().__init__(color, redraw_frequency_seconds, draw_smooth_graph)

    def set_new_values(self, values):
        normalized_values = self._normalize_values(values)
        return super().set_new_values(normalized_values)

    def _normalize_values(self, values):
        self._refresh_reference_value(values)

        normalized_values = []

        for value in values:
            normalized_value = self._calculate_normalized_value(value)
            normalized_values.append(normalized_value)

        return normalized_values

    def _calculate_normalized_value(self, value):
        if self._reference_value == 0:
            return 0

        return int(value * 100 / self._reference_value)

    def _refresh_reference_value(self, values):
        previous_own_reference_value = self._own_reference_value
        self._own_reference_value = max(max(values), self._minimum_reference_value)

        if previous_own_reference_value != self._own_reference_value:
            self._new_reference_value_callback(self._own_reference_value)

    def set_reference_value(self, value):
        self._reference_value = value
