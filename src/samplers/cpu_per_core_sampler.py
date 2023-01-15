import psutil
from statistics import mean

from .sampler import Sampler
from .sample import Sample


class CpuPerCoreSampler(Sampler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _get_sample(self):
        value_list = psutil.cpu_percent(percpu=True)

        int_values = list(map(int, value_list))
        sample = Sample(
            to_plot=int_values,
            single_value=int(mean(int_values)),
            units="%"
        )

        return sample
