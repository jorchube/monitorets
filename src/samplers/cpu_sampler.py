import psutil

from .sampler import Sampler
from .sample import Sample


class CpuSampler(Sampler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _get_sample(self):
        value = int(psutil.cpu_percent())
        sample = Sample(to_plot=value, single_value=value, units="%")
        return sample
