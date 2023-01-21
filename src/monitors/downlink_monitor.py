from .monitor import Monitor
from ..samplers.downlink_sampler import DownlinkSampler


class DownlinkMonitor(Monitor):
    def __init__(self):
        sampler = DownlinkSampler()
        super().__init__(sampler)
