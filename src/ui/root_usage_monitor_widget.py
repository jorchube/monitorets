from .monitor_widget import MonitorWidget
from ..samplers.disk_usage_sampler import DiskUsageSampler
from . import colors


class RootUsageMonitorWidget(MonitorWidget):
    def __init__(self, *args, **kwargs):
        title = "/"
        sampler = DiskUsageSampler("/")
        color = colors.PURPLE

        super().__init__(title, sampler, color, *args, **kwargs)
