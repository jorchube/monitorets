import psutil

from .sampler import Sampler


class CpuSampler(Sampler):
    def __init__(self):
        super().__init__()

    def _get_sample(self):
        value = psutil.cpu_percent()
        return int(value)
