from io import SEEK_SET

from .sampler import Sampler


class GpuSampler(Sampler):
    def __init__(self, file, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._path = file
        self._file_handle = open(self._path, "r")

    def _get_sample(self):
        value_read = self._read_file(self._file_handle)
        return int(value_read)

    def _read_file(self, file_handle):
        file_handle.seek(0, SEEK_SET)
        return file_handle.readline()
