import psutil

from .sampler import Sampler


class CpuSampler(Sampler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _get_sample(self):
        value = psutil.cpu_percent()
        return int(value)
