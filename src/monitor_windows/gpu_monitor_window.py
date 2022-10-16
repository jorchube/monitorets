from ..monitor_windows.monitor_window import MonitorWindow
from ..samplers.gpu_sampler import GpuSampler
from ..ui import colors
from ..monitor_type import MonitorType
from ..preferences import Preferences


class GPUMonitorWindow(MonitorWindow):
    def __init__(self, *args, **kwargs):
        title = "GPU"
        sampling_frequency = Preferences.get("gpu_monitor.sampling_frequency_seconds")
        sampler = GpuSampler("/sys/class/drm/card0/device/gpu_busy_percent", sampling_frequency_seconds=sampling_frequency)

        super().__init__(title, sampler, type=MonitorType.GPU, color=colors.GREEN, *args, **kwargs)
