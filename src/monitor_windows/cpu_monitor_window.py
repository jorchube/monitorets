from .monitor_window import MonitorWindow
from ..samplers.cpu_sampler import CpuSampler
from ..ui import colors
from ..monitor_type import MonitorType
from ..preferences import Preferences


class CPUMonitorWindow(MonitorWindow):
    def __init__(self, *args, **kwargs):
        title = "CPU"
        sampling_frequency = Preferences.get("cpu_monitor.sampling_frequency_seconds")
        sampler = CpuSampler(sampling_frequency)

        super().__init__(title, sampler, type=MonitorType.CPU, color=colors.BLUE, *args, **kwargs)
