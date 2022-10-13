from unittest import mock
import pytest

from ..samplers.sampler import Sampler


class TestSampler:
    @pytest.fixture
    def mock_read(self):
        with mock.patch("src.samplers.sampler.Sampler._get_sample") as mock_read:
            mock_read.return_value = 33
            yield mock_read

    @pytest.mark.usefixtures("mock_read")
    def test_it_samples_a_file(self):
        def new_sample_callback(value):
            global sample
            sample = value

        sampler = Sampler()
        sampler.install_new_sample_callback(new_sample_callback)

        sampler._sample()

        assert sample == 33
