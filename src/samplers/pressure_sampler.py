from io import SEEK_SET
import re
from .sampler import Sampler
from .sample import Sample


class PressureSampler(Sampler):
    def __init__(self, pressure_file_path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._file_handle = open(pressure_file_path, "r")
        self._regex = re.compile(".*avg10=(\d+\.\d\d).*")

    def _get_sample(self):
        line = self._read_line_from_file(self._file_handle)

        value = int(self._get_avg10_value(line))

        sample = Sample(to_plot=value, single_value=value, units="%")

        return sample

    def _read_line_from_file(self, file_handle):
        file_handle.seek(0, SEEK_SET)
        return file_handle.readline()

    def _get_avg10_value(self, line):
        matches = self._regex.match(line)
        return float(matches.group(1))
