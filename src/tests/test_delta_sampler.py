from ..samplers.delta_sampler import DeltaSampler

from time import sleep

class TestDeltaSampler:
    class _TestSampler(DeltaSampler):
        def __init__(self):
            self._sample_values = [1, 2, 5, 10, 20]
            self._sample_index = 0
            super().__init__(sampling_frequency_hz=20)

        def _get_sample(self):
            sample = self._sample_values[self._sample_index]
            self._sample_index += 1
            return sample

    def test_it_does_not_call_callback_on_first_sample(self):
        samples = []
        def mock_new_sample_callback(value):
            samples.append(value)

        test_sampler = self._TestSampler()
        test_sampler.install_new_sample_callback(mock_new_sample_callback)
        test_sampler._sample()

        assert samples == []

    def test_it_does_stores_delta_values_after_first_sample(self):
        samples = []
        def mock_new_sample_callback(value):
            samples.append(value)

        test_sampler = self._TestSampler()
        test_sampler.install_new_sample_callback(mock_new_sample_callback)
        test_sampler._sample()
        test_sampler._sample()
        test_sampler._sample()
        test_sampler._sample()
        test_sampler._sample()

        assert samples == [1, 3, 5, 10]
