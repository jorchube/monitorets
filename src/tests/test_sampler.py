from ..samplers.sampler import Sampler

from time import sleep

class TestSampler:
    class _TestSampler(Sampler):
        def __init__(self):
            self._samples_gotten = 0
            super().__init__(sampling_frequency_seconds=0.05)

        def _get_sample(self):
            self._samples_gotten = self._samples_gotten + 1
            return self._samples_gotten

    def test_it_samples_values_until_stopped(self):
        samples = []
        def mock_new_sample_callback(value):
            samples.append(value)

        test_sampler = self._TestSampler()
        test_sampler.install_new_sample_callback(mock_new_sample_callback)
        test_sampler.start()

        while len(samples) < 3:
            sleep(0.1)

        test_sampler.stop()

        assert [1, 2, 3] == samples[:3]
