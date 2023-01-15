import psutil

from .sampler import Sampler
from .sample import Sample


class SwapSampler(Sampler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _get_sample(self):
        swap = psutil.swap_memory()

        percent_value = int(swap.percent)
        single_value = self._to_GiB(swap.used)

        sample = Sample(
            to_plot=percent_value,
            single_value=round(single_value, 1),
            units="GiB"
        )

        return sample

    def _to_GiB(self, bytes) -> float:
        return bytes / (1024 * 1024 * 1024)
