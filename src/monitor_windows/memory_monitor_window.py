from ..monitor_windows.monitor_window import MonitorWindow
from ..samplers.memory_sampler import MemorySampler
from ..ui import colors
from ..monitor_type import MonitorType
from ..preferences import Preferences


class MemoryMonitorWindow(MonitorWindow):
    def __init__(self, *args, **kwargs):
        title = "Memory"
        sampling_frequency = Preferences.get("memory_monitor.sampling_frequency_seconds")
        sampler = MemorySampler(sampling_frequency_seconds=sampling_frequency)

        super().__init__(title, sampler, type=MonitorType.Memory, color=colors.ORANGE, *args, **kwargs)
