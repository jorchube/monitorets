import psutil

from .. import units
from .sampler import Sampler
from .sample import Sample


class SwapSampler(Sampler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _get_sample(self):
        swap = psutil.swap_memory()

        percent_value = int(swap.percent)
        single_value = units.convert(swap.used, units.Byte, units.GiB)

        sample = Sample(
            to_plot=percent_value,
            single_value=round(single_value, 1),
            units=units.GiB.unit,
        )

        return sample
