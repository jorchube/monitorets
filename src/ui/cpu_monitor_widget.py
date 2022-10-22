from .monitor_widget import MonitorWidget
from ..samplers.cpu_sampler import CpuSampler
from ..monitor_type import MonitorType
from . import colors


class CpuMonitorWidget(MonitorWidget):
    def __init__(self, *args, **kwargs):
        title = "CPU"
        sampler = CpuSampler()
        type = MonitorType.CPU
        color = colors.BLUE

        super().__init__(title, sampler, type, color, *args, **kwargs)
