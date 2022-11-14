from .sampler import Sampler


class DeltaSampler(Sampler):
    def __init__(self, sampling_frequency_hz=1):
        super().__init__(sampling_frequency_hz)
        self._previous_value = None

    def _sample(self):
        value = self._get_sample()

        if self._previous_value == None:
            self._previous_value = value
            return

        delta_value = value - self._previous_value
        self._previous_value = value

        self._sample_callback(delta_value)
