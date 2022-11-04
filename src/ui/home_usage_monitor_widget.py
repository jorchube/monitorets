from pathlib import Path
from .monitor_widget import MonitorWidget
from ..samplers.disk_usage_sampler import DiskUsageSampler
from ..monitor_type import MonitorType
from . import colors


class HomeUsageMonitorWidget(MonitorWidget):
    def __init__(self, *args, **kwargs):
        title = "~"
        sampler = DiskUsageSampler(self._home_path())
        type = MonitorType.Home_usage
        color = colors.PURPLE

        super().__init__(title, sampler, type, color, *args, **kwargs)

    def _home_path(self):
        return Path.home().absolute().as_posix()
