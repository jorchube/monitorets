from ..monitor_windows.monitor_window import MonitorWindow
from ..samplers.memory_sampler import MemorySampler
from ..ui import colors
from ..monitor_type import MonitorType


class MemoryMonitorWindow(MonitorWindow):
    def __init__(self, *args, **kwargs):
        title = "Memory"
        sampler = MemorySampler()

        super().__init__(title, sampler, type=MonitorType.Memory, color=colors.ORANGE, *args, **kwargs)
