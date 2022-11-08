from pathlib import Path
from .monitor_widget import MonitorWidget
from ..samplers.disk_usage_sampler import DiskUsageSampler
from . import colors


class HomeUsageMonitorWidget(MonitorWidget):
    def __init__(self, *args, **kwargs):
        title = "~"
        sampler = DiskUsageSampler(self._home_path())
        color = colors.PURPLE

        super().__init__(title, sampler, color, *args, **kwargs)

    def _home_path(self):
        return Path.home().absolute().as_posix()
