from .monitor import Monitor
from ..samplers.uplink_sampler import UplinkSampler


class UplinkMonitor(Monitor):
    def __init__(self):
        sampler = UplinkSampler()
        super().__init__(sampler)
