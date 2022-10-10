from unittest import mock
import pytest

from ..sampler import Sampler


class TestSampler:
    @pytest.fixture
    def mock_read(self):
        with mock.patch("src.sampler.Sampler._read") as mock_read:
            mock_read.return_value = 33
            yield mock_read

    @pytest.mark.usefixtures("mock_read")
    def test_it_samples_a_file(self):
        def new_sample_callback(value):
            global sample
            sample = value

        sampler = Sampler("/some/file", new_sample_callback)
        sampler._sample()

        assert sample == 33
