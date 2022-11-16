import psutil

from .delta_sampler import DeltaSampler


class UplinkSampler(DeltaSampler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _get_sample(self):
        per_nic_counters = psutil.net_io_counters(pernic=True)

        counter = 0
        for key, value in per_nic_counters.items():
            if key != 'lo':
                counter += value.bytes_sent

        return int(counter)
