import psutil

from .sampler import Sampler


class CpuPerCoreSampler(Sampler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _get_sample(self):
        value_list = psutil.cpu_percent(percpu=True)
        return list(map(int, value_list))
