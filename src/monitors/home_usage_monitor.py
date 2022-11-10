from .monitor import Monitor
from pathlib import Path
from ..samplers.disk_usage_sampler import DiskUsageSampler

class HomeUsageMonitor(Monitor):
    def __init__(self):
        sampler = DiskUsageSampler(self._home_path())
        super().__init__(sampler)

    def _home_path(self):
        return Path.home().absolute().as_posix()
