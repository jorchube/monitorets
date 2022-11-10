from .monitor import Monitor
from ..samplers.disk_usage_sampler import DiskUsageSampler

class RootUsageMonitor(Monitor):
    def __init__(self):
        sampler = DiskUsageSampler("/")
        super().__init__(sampler)
