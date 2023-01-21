from io import SEEK_SET

from .sampler import Sampler
from .sample import Sample


class GpuSampler(Sampler):
    def __init__(self, file, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._path = file
        self._file_handle = open(self._path, "r")

    def _get_sample(self):
        value = int(self._read_file(self._file_handle))

        sample = Sample(to_plot=value, single_value=value, units="%")

        return sample

    def _read_file(self, file_handle):
        file_handle.seek(0, SEEK_SET)
        return file_handle.readline()
