import psutil

from .sampler import Sampler


class DiskUsageSampler(Sampler):
    def __init__(self, path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._path = path

    def _get_sample(self):
        value_aggregate = psutil.disk_usage(self._path)
        value = value_aggregate.percent

        return int(value)
