from unittest import mock
import pytest
from ..samplers.pressure_sampler import PressureSampler


class TestPressureSampler:
    @pytest.fixture
    def file_handle_mock(self):
        m = mock.Mock()
        m.readline.return_value = """some avg10=7.71 avg60=0.00 avg300=1.03 total=154824318"""
        return m

    @pytest.fixture
    def mock_open(self, file_handle_mock):
        with mock.patch("builtins.open") as m:
            m.return_value = file_handle_mock
            yield m

    def test_it_returns_avg10_value_for_some_row(self, mock_open):
        delta_sampler = PressureSampler("test_file")

        sample = delta_sampler._get_sample()

        mock_open.assert_called_once_with("test_file", "r")
        assert sample.units == "%"
        assert sample.single_value == 7
        assert sample.to_plot == 7
