import psutil

from .delta_sampler import DeltaSampler


class UplinkSampler(DeltaSampler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _get_sample(self):
        counters = psutil.net_io_counters()
        sample = int(counters.bytes_sent)

        return sample
