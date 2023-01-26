import pytest

from ..monitors.monitor import Monitor
from ..samplers.sampler import Sampler
from ..samplers.sample import Sample


class TestMonitor:
    @pytest.fixture
    def samples(self):
        return [
            Sample(to_plot=1, single_value=1, units="unit"),
            Sample(to_plot=3, single_value=3, units="unit"),
            Sample(to_plot=5, single_value=5, units="unit"),
            Sample(to_plot=10, single_value=10, units="unit"),
            Sample(to_plot=20, single_value=20, units="unit"),
        ]

    @pytest.fixture
    def test_sampler(self, samples):
        class _TestSampler(Sampler):
            def __init__(self, sampling_frequency_hz=1):
                self.samples = samples
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
                return self._graph_values

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
        test_monitor._EXTRA_BUFFER_OF_STORED_SAMPLES = 0
        test_monitor.set_max_number_of_stored_samples(2)
        test_monitor.trigger_new_sample()
        test_monitor.trigger_new_sample()
        test_monitor.trigger_new_sample()
        test_monitor.trigger_new_sample()
        test_monitor.trigger_new_sample()

        values = test_monitor.get_values()

        assert values == [20, 10]
