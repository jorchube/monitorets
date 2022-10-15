from .monitor_window import MonitorWindow
from ..samplers.cpu_sampler import CpuSampler
from ..ui import colors
from ..monitor_type import MonitorType


class CPUMonitorWindow(MonitorWindow):
    def __init__(self, *args, **kwargs):
        title = "CPU"
        sampler = CpuSampler()

        super().__init__(title, sampler, type=MonitorType.CPU, color=colors.BLUE, *args, **kwargs)
