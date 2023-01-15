import psutil

from .sampler import Sampler
from .sample import Sample


class MemorySampler(Sampler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _get_sample(self):
        vmem = psutil.virtual_memory()

        available = vmem.available
        total = vmem.total
        used = total - available

        percent_value = int((used/total) * 100)
        single_value = self._to_GiB(used)

        sample = Sample(
            to_plot=percent_value,
            single_value=round(single_value, 1),
            units="GiB"
        )

        return sample

    def _to_GiB(self, bytes) -> float:
        return bytes / (1024 * 1024 * 1024)
