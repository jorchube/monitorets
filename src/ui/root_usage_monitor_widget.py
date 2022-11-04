from pathlib import Path
from .monitor_widget import MonitorWidget
from ..samplers.disk_usage_sampler import DiskUsageSampler
from ..monitor_type import MonitorType
from . import colors


class RootUsageMonitorWidget(MonitorWidget):
    def __init__(self, *args, **kwargs):
        title = "/"
        sampler = DiskUsageSampler("/")
        type = MonitorType.Root_usage
        color = colors.PURPLE

        super().__init__(title, sampler, type, color, *args, **kwargs)
