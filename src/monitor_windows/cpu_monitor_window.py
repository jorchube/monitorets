from ..monitor_windows.monitor_window import MonitorWindow
from ..samplers.cpu_sampler import CpuSampler
from ..ui import colors


class CPUMonitorWindow(MonitorWindow):
    def __init__(self, *args, **kwargs):
        title = "CPU"
        sampler = CpuSampler()

        super().__init__(title, sampler, color=colors.BLUE, *args, **kwargs)
