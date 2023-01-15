import psutil

from .. import units
from .sampler import Sampler
from .sample import Sample


class DiskUsageSampler(Sampler):
    def __init__(self, path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._path = path

    def _get_sample(self):
        usage = psutil.disk_usage(self._path)

        value_percent = usage.percent
        single_value = units.convert(usage.used, units.Byte, units.GiB)

        sample = Sample(
            to_plot=value_percent,
            single_value=round(single_value),
            units=units.GiB.unit
        )

        return sample
