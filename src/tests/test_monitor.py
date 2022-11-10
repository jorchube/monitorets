import pytest

from ..monitors.monitor import Monitor
from ..samplers.sampler import Sampler


class TestMonitor:
    @pytest.fixture
    def test_sampler(self):
        class _TestSampler(Sampler):
            def __init__(self, sampling_frequency_hz=1):
                super().__init__(sampling_frequency_hz)

            def take_sample(self):
                self._sample_callback(33)

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

            def _new_sample(self, value):
                self._sample = value

            def get_sample_value(self):
                return self._sample

        return _TestMonitor()


    def test_monitor_receives_new_sample_from_sampler(self, test_monitor):
        test_monitor.trigger_new_sample()

        sample_value = test_monitor.get_sample_value()

        assert sample_value == 33
