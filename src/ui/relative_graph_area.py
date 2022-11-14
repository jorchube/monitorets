from .graph_area import GraphArea


class RelativeGraphArea(GraphArea):
    def __init__(self, color, redraw_frequency_seconds):
        super().__init__(color, redraw_frequency_seconds)

    def set_new_values(self, values):
        normalized_values = self._normalize_values(values)
        return super().set_new_values(normalized_values)

    def _normalize_values(self, values):
        max_value = max(values)
        normalized_values = []

        for value in values:
            normalized_value = self._calculate_normalized_value(value, max_value)
            normalized_values.append(normalized_value)

        return normalized_values

    def _calculate_normalized_value(self, value, max_value):
        if max_value == 0:
            return 0

        return int(value * 100 / max_value)
