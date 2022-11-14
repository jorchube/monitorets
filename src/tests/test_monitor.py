import pytest

from ..monitors.monitor import Monitor
from ..samplers.sampler import Sampler


class TestMonitor:
    @pytest.fixture
    def test_sampler(self):
        class _TestSampler(Sampler):
            def __init__(self, sampling_frequency_hz=1):
                self.samples = [1, 3, 5, 10, 20]
                self.samples_index = 0
                super().__init__(sampling_frequency_hz)

            def take_sample(self):
                sample = self.samples[self.samples_index]
                self.samples_index += 1
                self._sample_callback(sample)

        return _TestSampler()

    @pytest.fixture
    def test_monitor(self, test_sampler):
        class _TestMonitor(Monitor):
            def __init__(self):
                self._sampler = test_sampler
                super().__init__(self._sampler)
                self._sample = None

            def trigger_new_sample(self):
                self._sampler.take_sample()

            def get_values(self):
                return self._values

        return _TestMonitor()


    def test_monitor_stores_one_sample_from_sampler(self, test_monitor):
        test_monitor.trigger_new_sample()

        values = test_monitor.get_values()

        assert values == [1]

    def test_monitor_stores_many_samples_from_sampler(self, test_monitor):
        test_monitor.trigger_new_sample()
        test_monitor.trigger_new_sample()
        test_monitor.trigger_new_sample()

        values = test_monitor.get_values()

        assert values == [5, 3, 1]

    def test_monitor_discards_samples_when_max_is_reached(self, test_monitor):
        test_monitor._MAX_NUMBER_OF_VALUES_STORED = 2
        test_monitor.trigger_new_sample()
        test_monitor.trigger_new_sample()
        test_monitor.trigger_new_sample()
        test_monitor.trigger_new_sample()
        test_monitor.trigger_new_sample()

        values = test_monitor.get_values()

        assert values == [20, 10]
