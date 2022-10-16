from io import SEEK_SET

from .sampler import Sampler


class GpuSampler(Sampler):
    def __init__(self, file, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._path = file

    def _get_sample(self):
        with open(self._path, "r") as opened_file:
            opened_file.seek(0, SEEK_SET)
            value_read = opened_file.readline()
            return int(value_read)
