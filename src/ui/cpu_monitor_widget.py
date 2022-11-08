from .monitor_widget import MonitorWidget
from ..samplers.cpu_sampler import CpuSampler
from . import colors


class CpuMonitorWidget(MonitorWidget):
    def __init__(self, *args, **kwargs):
        title = "CPU"
        sampler = CpuSampler()
        color = colors.BLUE

        super().__init__(title, sampler, color, *args, **kwargs)
