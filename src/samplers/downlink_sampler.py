import psutil

from .delta_sampler import DeltaSampler


class DownlinkSampler(DeltaSampler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _get_sample(self):
        counters = psutil.net_io_counters()
        sample = int(counters.bytes_recv)

        return sample
