from .sampler import Sampler


class DeltaSampler(Sampler):
    def __init__(self, sampling_frequency_hz=1):
        super().__init__(sampling_frequency_hz)
        self._previous_value = None

    def process_sample(self, value):
        if self._previous_value == None:
            self._previous_value = value
            return 0

        delta_value = value - self._previous_value
        self._previous_value = value

        return delta_value
